# -*- coding: utf-8 -*-
# from odoo import http


# class Lista-compra(http.Controller):
#     @http.route('/lista-compra/lista-compra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lista-compra/lista-compra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lista-compra.listing', {
#             'root': '/lista-compra/lista-compra',
#             'objects': http.request.env['lista-compra.lista-compra'].search([]),
#         })

#     @http.route('/lista-compra/lista-compra/objects/<model("lista-compra.lista-compra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lista-compra.object', {
#             'object': obj
#         })
