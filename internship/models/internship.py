# -*- coding: utf-8 -*-

from odoo import models, fields, api

class internship(models.Model):
	_name = 'internship.internship'
	_description = "Internship"

	first_name = fields.Char(string='Name')
	student_id = fields.Char(string='Student ID')
	major = fields.Char(string='Specialized Program')
	stu_phone = fields.Char(string='Mobile Number')
	stu_email = fields.Char(string='Email')
	company = fields.Char(string='Company Name')
	com_address = fields.Char(string='Company Address')
	com_phone = fields.Char(string='Telephone')
	fax = fields.Char(string='Fax')
	work_scope = fields.Char(string = 'Desired Working Scope')
	duration = fields.Char(string='Desired Internship Period')
	professor = fields.Char(string='TGGS Project Advisor (TGGS lecturer)')
	adv_phone = fields.Char(string='Phone')
	adv_email = fields.Char(string='Email')

	state = fields.Selection([('draft', 'Draft'), ('started', 'Started'), ('progress', 'In progress'),
							  ('finished', 'Done'), ], required=True, default='draft')

	@api.one
	def draft_progressbar(self):
		self.write({
			'state': 'draft'
		})

	@api.one
	def started_progressbar(self):
		self.write({
			'state': 'started'
		})

	@api.one
	def progress_progressbar(self):
		self.write({
			'state': 'progress'
		})

	@api.one
	def done_progressbar(self):
		self.write({
			'state': 'finished'
		})

