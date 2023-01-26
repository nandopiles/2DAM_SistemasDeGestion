# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Inventario(models.Model):
    _name = 'lista_compra.inventario'
    _description = 'Inventario'

    # el name es necesario ponerlo para que luego en la vista del módulo podamos relacionarlo mejor y salga ese campo
    name = fields.Char(string='Nombre Producto')
    cantidad = fields.Integer(string='Cantidad')
    tipo_producto = fields.Char(string='Tipo Producto')
    precio_unidad = fields.Float(string='Precio Unidad')

    compra_id = fields.One2many('lista_compra.compra', 'inventario_id', string='Compra ID')

    _order = 'precio_unidad'

    @api.constrains('name')
    def _validate_name(self):
        name_counts = self.search_count([('name', '=', self.name)])
        print(name_counts)
        if name_counts > 0:
            raise exceptions.ValidationError("Nombre ya existente!!")


class Compra(models.Model):
    _name = 'lista_compra.compra'
    _description = 'Compra'

    name = fields.Char(string='Título Compra')
    cantidad_compra = fields.Integer(string="Cantidad Comprada")
    fecha_compra = fields.Date(string="Fecha de Compra")

    inventario_id = fields.Many2one('lista_compra.inventario', string='Inventario ID')
    comprador_id = fields.Many2one('lista_compra.comprador', string='Comprador ID')

    _order = 'fecha_compra'


class Comprador(models.Model):
    _name = 'lista_compra.comprador'
    _description = 'Comprador'

    name = fields.Char(string='Nombre')
    apellido1 = fields.Char(string='Apellido 1')
    apellido2 = fields.Char(string='Apellido 2')
    direccion = fields.Char(string='Dirección')

    compra_id = fields.One2many('lista_compra.compra', 'inventario_id', string='Compra')
