# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StudentSubject(models.Model):
    _name = "student.subject"
    _inherit = "mail.thread"
    _description = "TGGS Subject"

    name = fields.Char('Name', size=128, required=True)
    code = fields.Char('Code', size=9, required=True)
    lec_hours = fields.Char('Lecture Hours', size=9)
    assign_self = fields.Char('Assignment and Self-Study', size=9)
    exam_prep = fields.Integer('Preparation for Exam', size=3)
    working_hrs = fields.Integer('Total Working Hours per Semester', size=3)
    ect_cred = fields.Integer('ECTS Credits', size=3)
    kmu_cred = fields.Char('KMUTNB Credits', size=12)
    # grade_weightage = fields.Float('Grade Weightage')
    subject_type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        'Subject Type', default="compulsory", required=True)
    state = fields.Selection([
        ('draft', 'Draft'), ('submitted', 'Submitted'),
        ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='draft', string='state', copy=False,
        track_visibility='onchange')

    _sql_constraints = [
        ('unique_subject_code',
         'unique(code)', 'Code should be unique per subject!'),
    ]

    # States for Approval by Backoffice Administrator

    @api.multi
    def action_reset_draft(self):
        self.state = 'draft'

    @api.multi
    def action_reject(self):
        self.state = 'rejected'

    @api.multi
    def action_submitted(self):
        self.state = 'submitted'

    @api.multi
    def action_approve(self):
        self.state = 'approve'

    # Subject Code
    @api.multi
    @api.constrains('code')
    def _check_code(self):
        for record in self:
            if record.code:
                if len(record.code) != 8:
                    raise ValidationError(_(
                        "[ERROR] Subject Code must be exactly 8 characters long"))

    # Notes : Electives have e.g. 090245xxxx
    @api.model
    def get_import_templates(self):
      return [{
         'label': _('Import Template for Subjects'),
         'template': '/aims_student_academic/static/xls/tggs_subject.xls'
     }]