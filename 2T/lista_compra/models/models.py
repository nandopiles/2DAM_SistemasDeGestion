# -*- coding: utf-8 -*-
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, exceptions


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

    inventario_id = fields.Many2one('lista_compra.inventario', string='Inventario')
    comprador_id = fields.Many2one('lista_compra.comprador', string='Comprador')

    _order = 'fecha_compra, comprador_id'


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

    pais_id = fields.Many2one(comodel_name='res.country', string='Pais')  # acceder a una tabla existente
    compra_id = fields.One2many('lista_compra.compra', 'inventario_id', string='Compra')

    _sql_constraints = [('nif_uniq', 'unique (nif)', "NIF repetido!")]

    @api.depends('fecha_nacimiento')
    def _age_compute(self):
        today = date.today()
        for record in self:
            record.edad = relativedelta(today, record.fecha_nacimiento).years
            print(str(record.edad))
