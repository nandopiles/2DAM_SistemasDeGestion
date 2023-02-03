# -*- coding: utf-8 -*-
# from odoo import http


# class HerenciaAlumno1(http.Controller):
#     @http.route('/herencia_alumno1/herencia_alumno1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/herencia_alumno1/herencia_alumno1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('herencia_alumno1.listing', {
#             'root': '/herencia_alumno1/herencia_alumno1',
#             'objects': http.request.env['herencia_alumno1.herencia_alumno1'].search([]),
#         })

#     @http.route('/herencia_alumno1/herencia_alumno1/objects/<model("herencia_alumno1.herencia_alumno1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('herencia_alumno1.object', {
#             'object': obj
#         })
