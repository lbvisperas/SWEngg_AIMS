# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StudentSubject(models.Model):
    _name = "student.subject"
    _inherit = "mail.thread"
    _description = "TGGS Subject"

    name = fields.Char('Name', size=128, required=True)
    code = fields.Char('Code', size=8, required=True)
    lec_hours = fields.Integer('Lecture Hours', size=3)
    assign_self = fields.Integer('Assignment and Self-Study', size=3)
    exam_prep = fields.Integer('Preparation for Exam', size=3)
    working_hrs = fields.Integer('Total Working Hours per Semester', size=3)
    ect_cred = fields.Integer('ECTS Credits', size=20)
    kmu_cred = fields.Integer('KMUTNB Credits', size=20)
    subject_type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        'Subject Type', default="compulsory", required=True)
    state = fields.Selection([
        ('draft', 'Draft'), ('submitted', 'Submitted'),
        ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='draft', string='state', copy=False,
        track_visibility='onchange')

    _sql_constraints = [
        ('unique_code',
         'unique(code)',
         '[ERROR] Code should be unique per subject!'),
        ('unique_name_code',
         'unique(code,name)',
         '[ERROR] Name should be unique per subject!'),
    ]

    # ensures that lecture hours, self assignment, exam preparation and working hours are not zero values
    @api.multi
    @api.constrains('lec_hours')
    def check_lec_hours(self):
        for record in self:
            if record.lec_hours:
                if record.lec_hours == 0:
                    raise ValidationError(_("[ERROR] Lecture hours cannot be a zero value"))

    @api.multi
    @api.constrains('assign_self')
    def check_assign_self(self):
        for record in self:
            if record.assign_self:
                if record.assign_self == 0:
                    raise ValidationError(_("[ERROR] Assignment hours cannot be a zero value"))

    @api.multi
    @api.constrains('exam_prep')
    def check_exam_prep(self):
        for record in self:
            if record.exam_prep:
                if record.exam_prep == 0:
                    raise ValidationError(_("[ERROR] Exam preparation cannot be a zero value"))

    # ensures that lecture hours, self assignment, exam preparation and working hours are not zero values
    @api.multi
    @api.constrains('kmu_cred')
    def check_credit_kmu(self):
        for record in self:
            if record.kmu_cred:
                if len(record.kmu_cred) < 1:
                    raise ValidationError(_("[ERROR] KMU Credits cannot be zero / empty value!"))
    @api.multi
    @api.constrains('ect_cred')
    def check_credit_ect(self):
        for record in self:
            if record.ect_cred:
                if len(record.ect_cred) < 1:
                    raise ValidationError(_("[ERROR] KMU Credits cannot be zero / empty value!"))

    # Subject Code
    @api.multi
    @api.constrains('code')
    def _check_code(self):
        for record in self:
            if record.code:
                if len(record.code) != 8:
                    raise ValidationError(_(
                        "[ERROR] Subject Code must be exactly 8 characters long"))
                if record.code == 0:
                    raise ValidationError(_(
                        "[ERROR] Subject Code must not be zero."))

    # States for Approval/ Reject by Backoffice Administrator
    # States for Reset Draft and Submitted by Faculty

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


    @api.model
    def get_import_templates(self):
      return [{
         'label': _('Import Template for Subjects'),
         'template': '/aims_student_academic/static/xls/tggs_subject.xls'
     }]