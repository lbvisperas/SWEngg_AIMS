# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VisaConference(models.Model):
      _name = 'visa.conference'

      first_name = fields.Char("First Name")
      middle_name = fields.Char("Middle Name")
      last_name = fields.Char("Last Name")
      student_id = fields.Integer()
      level_of_study = fields.Selection([
            ('masters', 'Masters'),
            ('doctoral', 'Doctoral'),
      ], string='Study Level', required=True)
      major = fields.Char("Major")
      home_address = fields.Text("Address")
      publication_entitled = fields.Text("Publication Entitled")
      conference_name = fields.Char("Conference Name")
      address_country = fields.Text("Address/Country")
      conference_date_start= fields.Date("Conference Date Start")
      conference_date_end= fields.Date("Conference Date End")
      tggs_advisor_name= fields.Char("TGGS Adviser Name")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100