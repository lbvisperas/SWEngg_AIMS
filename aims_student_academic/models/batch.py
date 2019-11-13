# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
#from odoo.exceptions import ValidationError


class StudentBatch(models.Model):
    _name = "student.batch"
    _inherit = "mail.thread"
    _description = "TGGS batch"

    name = fields.Char('Name', size=32, required=True)
    year = fields.Char('Year', size=4, required=True)
    semester = fields.Selection([
        ('first semester', 'First Semester'),
        ('second semester', 'Second Semester'),
        ('summer semester', 'Summer Semester'),
    ], 'Semester', default='first semester')
    start_date = fields.Date('Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date('End Date', required=True)
    course_id = fields.Many2one('student.course', 'Course', required=True)