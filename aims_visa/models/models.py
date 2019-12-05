# -*- coding: utf-8 -*-

from odoo import models, fields, api

class visa(models.Model):
      _name = 'visa.visa'

      first_name = fields.Char("First Name")
      middle_name= fields.Char("Middle Name")
      last_name = fields.Char("Last Name")
      student_id=fields.Integer()
      nationality= fields.Char("Nationality")
      passport_num=fields.Char("Passport Number")
      visa_num=fields.Char("Visa Number")
      visa_issue_date=fields.Date("Visa Issue Date")
      visa_expiry_date=fields.Date("Visa Expiry Date")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100