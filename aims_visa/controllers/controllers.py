# -*- coding: utf-8 -*-
from odoo import http

# class Visa(http.Controller):
#     @http.route('/visa/visa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/visa/visa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('visa.listing', {
#             'root': '/visa/visa',
#             'objects': http.request.env['visa.visa'].search([]),
#         })

#     @http.route('/visa/visa/objects/<model("visa.visa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('visa.object', {
#             'object': obj
#         })