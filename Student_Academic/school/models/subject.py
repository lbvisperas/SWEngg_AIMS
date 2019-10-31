# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StudentSubject(models.Model):
    _name = "student.subject"
    _inherit = "mail.thread"
    _description = "TGGS Subject"

    name = fields.Char('Name', size=128, required=True)
    code = fields.Char('Code', size=256, required=True)
    # course = fields.Many2one('student.course', 'Course', required=True)
    # grade_weightage = fields.Float('Grade Weightage')
    type = fields.Selection(
        [('theory', 'Theory'), ('practical', 'Practical'),
         ('both', 'Both'), ('other', 'Other')],
        'Type', default="theory", required=True)
    subject_type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        'Subject Type', default="compulsory", required=True)

    _sql_constraints = [
        ('unique_subject_code',
         'unique(code)', 'Code should be unique per subject!'),
    ]

   # @api.model
    # def get_import_templates(self):
      #  return [{
       #     'label': _('Import Template for Subjects'),
       #     'template': '/openeducat_core/static/xls/op_subject.xls'
       # }]
