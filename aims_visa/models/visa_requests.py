# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VisaRequests(models.Model):
      _name = 'visa.requests'

      first_name = fields.Char("First Name")
      middle_name = fields.Char("Middle Name")
      last_name = fields.Char("Last Name")
      nationality = fields.Char("Nationality")
      country = fields.Char("Country")
      student_id = fields.Integer()
      level_of_study = fields.Selection([
            ('masters', 'Masters'),
            ('doctoral', 'Doctoral'),
      ], string='Study Level', required=True)
      major = fields.Char("Major")
      passport_num = fields.Char("Passport Number")
      passport_valid_until = fields.Date("Valid Until")
      reason_for_visit = fields.Text("Reason Visit")
      period_of_stay = fields.Integer("Period")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100