# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Parque(models.Model):
    _name = 'pileslablanca.parque'
    _description = 'Parque'

    name = fields.Char(string='Nombre Parque')
    jefe = fields.Char(string='Jefe')
    direccion = fields.Char(string='Dirección')
    fecha_inauguracion = fields.Date(string='Fecha Inauguración')
    num = fields.Integer(string='Num')
    es_viejo = fields.Boolean(string='¿Es viejo?')
    otro_dato = fields.Integer(string='Otro Dato')
    tamanyo = fields.Selection([('Grande', 'Grande'), ('Pequenyo', 'Pequenyo')])


class Bombero(models.Model):
    _name = 'pileslablanca.bombero'
    _description = 'Bombero'

    name = fields.Char(string='DNI')
    nombre = fields.Char(string='Nombre')
    apellido1 = fields.Char(string='Apellido 1')
    apellido2 = fields.Char(string='Apellido 2')
    es_veterano = fields.Boolean(string='Veterano')
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    salario = fields.Integer(string='Salario')
    sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')])

    parque_id = fields.Many2one('pileslablanca.parque', string="Parque")
    # bomberocamion_id = fields.One2many('pileslablanca.bomberocamion', 'bombero', string='Bomberocamion')

    _order = 'apellido1'


class Camion(models.Model):
    _name = 'pileslablanca.camion'
    _description = 'Camion'

    name = fields.Char(string='Matrícula')
    cv = fields.Integer(string='CV')
    litros = fields.Float(string='Litros')
    color = fields.Selection([('Rojo', 'Rojo'), ('Amarillo', 'Amarillo')])
    capacidad = fields.Integer(string='Capacidad')
    lleva_manguera = fields.Boolean(string='¿Lleva manguera?')
    otro_campo = fields.Char(string='Campo Ejemplo')

    parque_id = fields.Many2one('pileslablanca.parque', string="Parque")

    _sql_constraints = [('name_matricula_uniq', 'unique (name)', "Matrícula Repetida!")]

    debe_repostar = fields.Boolean(string='Necesita repostar', compute='_compute_under_fuel')

    @api.onchange('litros')
    def _compute_under_fuel(self):
        if self.litros < 15:
            self.debe_repostar = True
        else:
            self.debe_repostar = False


class Bomberocamion(models.Model):
    _name = 'pileslablanca.bomberocamion'
    _description = 'Bomberocamion'

    bombero_id = fields.Many2one('pileslablanca.bombero', string="Bombero")
    camion_id = fields.Many2one('pileslablanca.camion', string="Camion")
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_fin = fields.Date(string='Fecha Fin')
    puesto = fields.Selection([('Manguera', 'Manguera'), ('Parque', 'Parque'), ('Informatico', 'Informatico')])
