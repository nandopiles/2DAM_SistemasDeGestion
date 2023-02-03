# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'herencia_alumno1.alumno'
    _description = 'herencia_alumno1.Alumno'

    name = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')])

    asignaturas_ids = fields.Many2many('herencia_alumno1.asignatura', string="Asignaturas")


class Asignatura(models.Model):
    _name = 'herencia_alumno1.asignatura'
    _description = 'herencia_alumno1.Asignatura'

    name = fields.Char(string="Asginatura")
    horas = fields.Integer(string="Horas Lectivas")

    alumnos_ids = fields.Many2many('herencia_alumno1.alumno', string="Alumnos")
