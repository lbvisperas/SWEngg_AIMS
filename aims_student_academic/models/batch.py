# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentBatch(models.Model):
    _name = "student.batch"
    _inherit = "mail.thread"
    _description = "TGGS batch"

    name = fields.Char('Name', size=256, default='SSE_2010_First_Semester')
    year = fields.Char('Year', size=4, required=True, default='2019')
    semester = fields.Selection([
        ('First_Semester', 'First_Semester'),
        ('Second_Semester', 'Second_Semester'),
        ('Summer_Semester', 'Summer_Semester'),
    ], 'Semester', default='First_Semester')
    start_date = fields.Date('Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date('End Date', required=True)
    course_id = fields.Many2one('student.course', 'Course', required=True, default='Software Systems Engineering')

    _sql_constraints = [(
        'unique_name',
        'unique(name)',
        '[ERROR] Batch already exists. Batches must only have one entry! '
    )]

    @api.multi
    @api.onchange('course_id', 'year', 'semester')
    def batch_name(self):
        for record in self:
            record.name = (str(record.course_id.code) or ' ') + '_' + (str(record.year) or ' ') + '_' + (str(record.semester) or ' ')

    @api.multi
    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for record in self:
            start_date = fields.Date.from_string(record.start_date)
            end_date = fields.Date.from_string(record.end_date)
            if start_date > end_date:
                raise ValidationError(
                    _("End Date cannot be set before Start Date."))

