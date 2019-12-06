# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentInternship(models.Model):
	_name = 'student.internship'
	_description = "Internship"
	_inherit = ["mail.thread"]

	first_name = fields.Many2one('student.student', 'Student', required=True, track_visibility='onchange') #based on student_academic
	student_id = fields.Char(string='Student ID') #based on student_academic
	major = fields.Char(string='Specialized Program') # based on student_academic
	stu_phone = fields.Char(string='Mobile Number') #based on student_academic
	stu_email = fields.Char(string='Email') #based on student_academic
	company = fields.Char(string='Company Name') #create spearate model for this as company.py
	com_address = fields.Char(string='Company Address')  #create spearate model for this as company.py
	com_phone = fields.Char(string='Telephone')  #create spearate model for this as company.py
	fax = fields.Char(string='Fax')
	work_scope = fields.Char(string = 'Desired Working Scope')
	duration = fields.Char(string='Desired Internship Period')
	professor = fields.Many2one('student.faculty', 'Professor', required=True, track_visibility='onchange')  #based on faculty => create separate model advisor.py that inherits faculty
	adv_phone = fields.Char(string='Phone') #based on faculty => create separate model advisor.py that inherits faculty
	adv_email = fields.Char(string='Email') #based on faculty => create separate model advisor.py that inherits faculty

	state = fields.Selection([('started', 'Started'), ('finished', 'Done')])

	@api.one
	def started_progressbar(self):
		self.write({
			'state': 'started'
		})


	@api.one
	def done_progressbar(self):
		self.write({
			'state': 'finished'
		})

