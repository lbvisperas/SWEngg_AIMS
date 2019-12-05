# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VisaInternship(models.Model):
      _name = 'visa.internship'

      first_name = fields.Char("First Name")
      middle_name = fields.Char("Middle Name")
      last_name = fields.Char("Last Name")
      student_id = fields.Integer()
      level_of_study = fields.Selection([
            ('masters', 'Masters'),
            ('doctoral', 'Doctoral'),
      ], string='Study Level', required=True)
      major = fields.Char("Major")
      home_address = fields.Char("Address")
      company_name = fields.Char("Company Name")
      company_address_country = fields.Char("Company Address Country")
      internship_duration_start= fields.Date("Internship Duration Start")
      internship_duration_end= fields.Date("Internship Duration End")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100