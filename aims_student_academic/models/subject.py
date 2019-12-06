# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StudentSubject(models.Model):
    _name = "student.subject"
    _inherit = "mail.thread"
    _description = "TGGS Subject"

    name = fields.Char('Name', size=128, required=True)
    code = fields.Char('Code', size=9, required=True)
    lec_hours = fields.Char('Lecture Hours', size=64)
    assign_self = fields.Char('Assignment and Self-Study', size=64)
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