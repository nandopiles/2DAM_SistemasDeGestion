# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Profesor(models.Model):
    _name = 'herencia_alumno2.profesor'
    _description = 'herencia_alumno2.Profesor'

    name = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")

    asignaturas_ids = fields.One2many('herencia_alumno1.asignatura', 'profesor_id', string='Asignaturas')
