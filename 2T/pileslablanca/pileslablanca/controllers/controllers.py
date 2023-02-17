# -*- coding: utf-8 -*-
# from odoo import http


# class Pileslablanca(http.Controller):
#     @http.route('/pileslablanca/pileslablanca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pileslablanca/pileslablanca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pileslablanca.listing', {
#             'root': '/pileslablanca/pileslablanca',
#             'objects': http.request.env['pileslablanca.pileslablanca'].search([]),
#         })

#     @http.route('/pileslablanca/pileslablanca/objects/<model("pileslablanca.pileslablanca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pileslablanca.object', {
#             'object': obj
#         })
