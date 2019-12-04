# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentSection(models.Model):
    _name = "student.section"
    _inherit = "mail.thread"
    _description = "Section"
    _order = "submission_date DESC"

    name = fields.Char('Section', size=64, required=True)
    course_id = fields.Many2one('student.course', 'Course', required=True)
    batch_id = fields.Many2one('student.batch', 'Batch', required=True)
    subject_id = fields.Many2one('student.subject', 'Subject', required=True)
    faculty_id = fields.Many2one('student.faculty', 'Faculty', required=True)
    marks = fields.Float('Marks', required=True, track_visibility='onchange')
    description = fields.Text('Description', required=True)
    state = fields.Selection([
        ('draft', 'Draft'), ('publish', 'Published'),
        ('finish', 'Finished'), ('cancel', 'Cancel'),
    ], 'State', required=True, default='draft', track_visibility='onchange')
    issued_date = fields.Datetime(string='Issued Date', required=True,
                                  default=lambda self: fields.Datetime.now())
    submission_date = fields.Datetime('Submission Date', required=True,
                                      track_visibility='onchange')
    allocation_ids = fields.Many2many('student.student', string='Allocated To')
    assignment_sub_line = fields.One2many('student.list.grades', 'assignment_id', 'Submissions')
    reviewer = fields.Many2one('student.affairs', 'Reviewer')

    @api.multi
    @api.constrains('issued_date', 'submission_date')
    def check_dates(self):
        for record in self:
            issued_date = fields.Date.from_string(record.issued_date)
            submission_date = fields.Date.from_string(record.submission_date)
            if issued_date > submission_date:
                raise ValidationError(_(
                    "Submission Date cannot be set before Issue Date."))

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False
        if self.course_id:
            subject_ids = self.env['student.course'].search([
                ('id', '=', self.course_id.id)]).subject_ids
            return {'domain': {'subject_id': [('id', 'in', subject_ids.ids)]}}

    @api.multi
    def act_publish(self):
        result = self.state = 'publish'
        return result and result or False

    @api.multi
    def act_finish(self):
        result = self.state = 'finish'
        return result and result or False

    @api.multi
    def act_cancel(self):
        self.state = 'cancel'

    @api.multi
    def act_set_to_draft(self):
        self.state = 'draft'
