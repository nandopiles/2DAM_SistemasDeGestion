# -*- coding: utf-8 -*-
# from odoo import http


# class Practica4(http.Controller):
#     @http.route('/practica4/practica4/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practica4/practica4/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practica4.listing', {
#             'root': '/practica4/practica4',
#             'objects': http.request.env['practica4.practica4'].search([]),
#         })

#     @http.route('/practica4/practica4/objects/<model("practica4.practica4"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practica4.object', {
#             'object': obj
#         })
