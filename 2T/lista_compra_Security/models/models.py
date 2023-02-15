# -*- coding: utf-8 -*-
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError


class Inventario(models.Model):
    _name = 'lista_compra.inventario'
    _description = 'Inventario'

    # el name es necesario ponerlo para que luego en la vista del módulo podamos relacionarlo mejor y salga ese campo
    name = fields.Char(string='Nombre Producto')
    cantidad = fields.Integer(string='Cantidad')
    tipo_producto = fields.Char(string='Tipo Producto')
    precio_unidad = fields.Float(string='Precio Unidad')

    compra_id = fields.One2many('lista_compra.compra', 'inventario_id', string='Compra')

    _sql_constraints = [('name_product_uniq', 'unique (name)', "Nombre del Producto Repetido!")]

    _order = 'precio_unidad'


class Compra(models.Model):
    _name = 'lista_compra.compra'
    _description = 'Compra'

    name = fields.Char(string='Título Compra')
    cantidad_compra = fields.Integer(string="Cantidad Comprada")
    fecha_compra = fields.Date(string="Fecha de Compra")
    metodo_compra = fields.Selection([('Tarjeta', 'Tarjeta'), ('Efectivo', 'Efectivo')], string="Método de Pago")

    inventario_id = fields.Many2one('lista_compra.inventario', string='Inventario')
    comprador_id = fields.Many2one('lista_compra.comprador', string='Comprador')

    _order = 'fecha_compra, comprador_id'

    @api.constrains('inventario_id', 'cantidad_compra')
    def _check_stock(self):
        stock = self.inventario_id.cantidad
        producto = self.inventario_id.name
        cantidad = self.cantidad_compra
        mensaje = None

        if cantidad > 0:
            if stock < 0:
                mensaje = "There is not stock --> " + str(producto)
                print(mensaje)
                raise ValidationError(mensaje)
            else:
                mensaje = "Stock of " + str(producto) + " exists"
                print(mensaje)
                if stock < cantidad:
                    mensaje = "[-] Not enough stock: " + str(stock) + "(Stock) " + str(cantidad) + "(Cantidad)"
                    print(mensaje)
                    raise ValidationError(mensaje)
                else:
                    mensaje = "[+] Enough stock: " + str(stock) + "(Stock) vs " + str(cantidad) + "(Cantidad)"
                    print(mensaje)
                    self._discount_amount()
        else:
            mensaje = "[-] You can't buy" + str(cantidad) + "(Unids)"
            print(mensaje)
            raise ValidationError(mensaje)

    def _discount_amount(self):
        stockSinDescontar = self.inventario_id.cantidad
        cantidad = self.cantidad_compra

        print("Stock sin descontar --> " + str(stockSinDescontar))
        print("Cantidad Compra --> " + str(cantidad))

        self.inventario_id.cantidad = stockSinDescontar - cantidad
        print("Stock Actualizado: " + str(stockSinDescontar - cantidad))


class Comprador(models.Model):
    _name = 'lista_compra.comprador'
    _description = 'Comprador'

    name = fields.Char(string='Nombre')
    nif = fields.Char(string='NIF')
    nif_tutor = fields.Text(string="NIF Tutor")
    apellido1 = fields.Char(string='Apellido 1')
    apellido2 = fields.Char(string='Apellido 2')
    direccion = fields.Char(string='Dirección')
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    edad = fields.Integer(string='Edad', compute='_age_compute')
    isMayorEdad = fields.Boolean(string='Mayor de Edad', compute='_compute_adult')
    limite_dinero = fields.Integer(string="Límite de dinero")
    dinero_gastado = fields.Float(string="Dinero Gastado", compute="_calculate_spent_money")

    pais_id = fields.Many2one(comodel_name='res.country', string='Pais')  # acceder a una tabla existente
    compra_id = fields.One2many('lista_compra.compra', 'inventario_id', string='Compra')

    _sql_constraints = [('nif_uniq', 'unique (nif)', "NIF repetido!")]

    @api.depends('fecha_nacimiento')
    def _age_compute(self):
        today = date.today()
        for record in self:
            record.edad = relativedelta(today, record.fecha_nacimiento).years
            print(str(record.edad))

    @api.onchange('edad')
    def _compute_adult(self):
        if self.edad >= 18:
            self.isMayorEdad = True
        else:
            self.isMayorEdad = False

    @api.depends('compra_id')
    def _calculate_spent_money(self):
        dinero_gastado = 0
        compras = self.compra_id

        if compras:
            for compra in compras:
                cliente_nombre = self.name
                producto_nombre = compra.inventario_id.name
                producto_precio = compra.inventario_id.precio_unidad
                compra_cantidad = compra.cantidad_compra
                limite_dinero = self.limite_dinero

                coste_total = producto_precio * compra_cantidad

                if coste_total > limite_dinero:
                    mensaje = "[-] Límite de dinero alcanzado!"
                    print(mensaje)
                    raise ValidationError(mensaje)
                else:
                    print(str(cliente_nombre) + " --> " + str(compra_cantidad) + " unidades, " + str(
                        producto_nombre) + " a " + str(
                        producto_precio) + " la unidad --> Coste Total: " + str(coste_total))
                    dinero_gastado += coste_total

                    self.dinero_gastado = dinero_gastado
        else:
            print("No hay compras registradas!")
            self.dinero_gastado = 0
