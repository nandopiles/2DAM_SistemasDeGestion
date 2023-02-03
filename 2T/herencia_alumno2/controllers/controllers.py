# -*- coding: utf-8 -*-
# from odoo import http


# class HerenciaAlumno2(http.Controller):
#     @http.route('/herencia_alumno2/herencia_alumno2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/herencia_alumno2/herencia_alumno2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('herencia_alumno2.listing', {
#             'root': '/herencia_alumno2/herencia_alumno2',
#             'objects': http.request.env['herencia_alumno2.herencia_alumno2'].search([]),
#         })

#     @http.route('/herencia_alumno2/herencia_alumno2/objects/<model("herencia_alumno2.herencia_alumno2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('herencia_alumno2.object', {
#             'object': obj
#         })
