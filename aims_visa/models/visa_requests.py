# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VisaRequests(models.Model):
      _name = 'visa.requests'

      first_name = fields.Char("First Name")
      student_id=fields.Integer()
      reason_for_visit=fields.Text("Reason Visit")
      period_of_stay= fields.Integer("Period")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100