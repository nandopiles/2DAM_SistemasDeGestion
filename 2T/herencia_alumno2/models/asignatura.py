# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Asignatura(models.Model):
    _inherit = 'herencia_alumno1.asignatura'

    profesor_id = fields.Many2one('herencia_alumno2.profesor', string='Profesor')
