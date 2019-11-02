# -*- coding: utf-8 -*-
from odoo import http

# class Internship(http.Controller):
#     @http.route('/internship/internship/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/internship/internship/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('internship.listing', {
#             'root': '/internship/internship',
#             'objects': http.request.env['internship.internship'].search([]),
#         })

#     @http.route('/internship/internship/objects/<model("internship.internship"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('internship.object', {
#             'object': obj
#         })