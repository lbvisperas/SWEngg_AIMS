# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
#from odoo.exceptions import ValidationError


class StudentBatch(models.Model):
    _name = "student.batch"
    _inherit = "mail.thread"
    _description = "TGGS batch"

    code = fields.Char('Code', size=16, required=True)
    name = fields.Char('Name', size=32, required=True)
    start_date = fields.Date(
        'Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date('End Date', required=True)
    course_id = fields.Many2one('student.course', 'Course', required=True)

    _sql_constraints = [
        ('unique_batch_code',
         'unique(code)', 'Code should be unique per batch!')]