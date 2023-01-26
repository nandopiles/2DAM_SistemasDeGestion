# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Car(models.Model):
    _name = 'prueba2.car'
    _description = 'Coche'

    name = fields.Char(string='Modelo')
    number_plate = fields.Char(string='Matrícula')
    cv = fields.Float(string='CV')
    colour = fields.Char(string='Color')
    fuel_litres = fields.Float(string='Litros')

    brand_id = fields.Many2one('prueba2.brand', string='Marca')


class Brand(models.Model):
    _name = 'prueba2.brand'
    _description = 'Marca'

    name = fields.Char(string='Nombre Marca')
    luxury = fields.Boolean(string='Lujo')

    cars_ids = fields.One2many('prueba2.car', 'brand_id', string='Coches de la Marca')

#    @api.depends('value')
#   def _value_pc(self):
#      for record in self:
#         record.value2 = float(record.value) / 100
