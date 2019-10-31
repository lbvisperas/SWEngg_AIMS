# -*- coding: utf-8 -*-
from odoo import http

class Registration(http.Controller):
     @http.route('/registration/registration/', auth='public')
     def index(self, **kw):
         return "Hello, world"

#     @http.route('/registration/registration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('registration.listing', {
#             'root': '/registration/registration',
#             'objects': http.request.env['registration.registration'].search([]),
#         })

#     @http.route('/registration/registration/objects/<model("registration.registration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registration.object', {
#             'object': obj
#         })