# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Parque(models.Model):
    _name = 'parque_bomberos.parque'
    _description = 'Parque'

    # el name es necesario ponerlo para que luego en la vista del módulo podamos relacionarlo mejor y salga ese campo
    name = fields.Char(string='Nombre Parque')
    jefe = fields.Char(string='Jefe')
    direccion = fields.Char(string='Dirección')
    fecha_inauguracion = fields.Date(string='Fecha Inauguración')
    ciudad = fields.Char(string='Ciudad')
    municipio = fields.Char(string='Municipio')

    camion = fields.One2many('parque_bomberos.camion', 'parque', string='Camion')


class Camion(models.Model):
    _name = 'parque_bomberos.camion'
    _description = 'Camion'

    name = fields.Char(string='Matrícula')
    cv = fields.Integer(string='CV')
    litros = fields.Float(string='Litros')
    color = fields.Char(string='Color')
    capacidad = fields.Integer(string='Capacidad')
    lleva_manguera = fields.Boolean(string='¿Lleva manguera?')

    parque = fields.Many2one('parque_bomberos.parque', string='Parque')
    bombero = fields.One2many('parque_bomberos.bombero', 'camion', string='Bombero')

    under_fuel = fields.Boolean(string='Necesita repostar', compute='_compute_under_fuel')

    @api.onchange('litros')
    def _compute_under_fuel(self):
        for record in self:
            if record.litros < 50:
                record.under_fuel = True
            else:
                record.under_fuel = False

    @api.constrains('cv', 'litros')
    def _validate_cv(self):
        if self.cv <= 0 and self.litros <= 0:
            raise exceptions.ValidationError('Litros y CV no PUEDEN ser menor o igual a 0!!')
        elif self.litros <= 0:
            raise exceptions.ValidationError('Litros no puede ser <= 0')
        elif self.cv <= 0:
            raise exceptions.ValidationError('CV no puede ser <= 0')


class Bombero(models.Model):
    _name = 'parque_bomberos.bombero'
    _description = 'Bombero'

    name = fields.Char(string='DNI')
    nombre = fields.Char(string='Nombre')
    apellidos = fields.Char(string='Apellidos')
    es_veterano = fields.Boolean(string='Veterano')
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    salario = fields.Integer(string='Salario')

    camion = fields.Many2one('parque_bomberos.camion', string='Camion')
