# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields, api, exceptions
from dateutil.relativedelta import *
from datetime import date

class Parque(models.Model):
    _name = 'odoo_model_practica4.parque'
    _description = 'Parque_bomberos'

    name = fields.Char(string='Modelo')
    año_fundacion = fields.Date(string='Fecha fundacion')
    localidad = fields.Char(string='Localidad')
    barras = fields.Boolean(string='Barras')
    recargas_camiones = fields.Integer(string='Nº recargas')
    camiones_ids = fields.One2many('odoo_model_practica4.camion', 'parque_id', string='camiones')


class Camion(models.Model):
    _name = 'odoo_model_practica4.camion'
    _description = 'Camion_Bomberos'

    number_plate = fields.Char(string='Matrícula')
    ruedas = fields.Integer(string='Nº Ruedas')
    capacidad_b = fields.Integer(string='NºBomberos')
    litros = fields.Integer(string='litros')
    antiguedad = fields.Integer(string='antiguedad')
    kilometros = fields.Integer(string='kilometros')
    bomberos_ids = fields.One2many('odoo_model_practica4.bomberos', 'camion_id', string='bomberos')
    parque_id = fields.Many2one('odoo_model_practica4.parque', string='parque')


class Bomberos(models.Model):
    _name = 'odoo_model_practica4.bomberos'
    _description = 'Bomberos'

    name = fields.Char(string='Modelo')
    edad = fields.Integer(string='Edad')
    cumple= fields.Date(string='dia de cumple')
    direccion = fields.Char(string='Direccion')
    sueldo = fields.Integer(string="Sueldo")
    inicio_trabajo = fields.Date(string='Inicio trabajo')
    puesto = fields.Selection([('conductor', 'Conductor'), ('pasajero', 'Pasajero'), ('encargado_manguera', 'Encargado de la manguera')])
    camion_id = fields.Many2one('odoo_model_practica4.camion', string='camion')
    age = fields.Integer(string='Age', compute='_age_compute')

    @api.depends('cumple')
    def _age_compute(self):
         today = date.today()
         for record in self:
             record.age = relativedelta(today, record.cumple).years
             print(str(record.age))