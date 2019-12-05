# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StudentCourse(models.Model):
    _name = "student.course"
    _inherit = "mail.thread"
    _description = "TGGS Courses"

    name = fields.Char('Name', size=128, required=True)
    code = fields.Char('Code (e.g.SSE,EPE', size=4, required=True)
    parent_id = fields.Many2one('student.course', 'Department')
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('GPA', 'GPA'),
         ('CWA', 'CWA'), ('CCE', 'CCE')],
        'Evaluation Type', default="normal", required=True)
    subject_ids = fields.Many2many('student.subject', string='Subject(s)')
    coordinator = fields.Many2one('student.faculty', string='Coordinator')
    max_unit_load = fields.Float("Maximum Unit Load", size=4)
    min_unit_load = fields.Float("Minimum Unit Load",  size=4)
    batch_id = fields.Many2many('student.batch', string='Batches')

    _sql_constraints = [
        ('unique_course_code',
         'unique(code)',
         '[ERROR] Code should be unique per course!'),
        ('unique_name',
         'unique(name)',
         '[ERROR] Name should be unique per subject!')
    ]

    @api.multi
    @api.constrains('mix_unit_load', 'max_unit_load')
    def constrain_course_details(self):
        for record in self:
            if len(record.min_unit_load) > 4:
                raise ValidationError(_(
                    "[ERROR] Min Unit load cannot greater than 4 characters"))
            if len(record.min_unit_load) < 1:
                raise ValidationError(_(
                    "[ERROR] Min Unit load cannot be less than 1 character"))
            if len(record.max_unit_load) > 4:
                raise ValidationError(_(
                    "[ERROR] Max Unit load cannot greater than 4 characters"))
            if len(record.max_unit_load) < 1:
                raise ValidationError(_(
                    "[ERROR] Max Unit load cannot be less than 1 character"))

    @api.multi
    @api.constrains('name')
    def name_check(self):
        for record in self:
            if len(record.name) > 128:
                raise ValidationError(_(
                    "[ERROR] Name cannot be greater than 128 characters"))
            if len(record.name) < 1:
                raise ValidationError(_(
                    "[ERROR] Name cannot be less than 1 character"))

    @api.multi
    @api.constrains('code')
    def code_check(self):
        for record in self:
            if len(record.code) > 4:
                raise ValidationError(_(
                    "[ERROR] Code cannot be greater than 4 characters"))
            if len(record.code) < 1:
                raise ValidationError(_(
                    "[ERROR] Code cannot be less than 1 character"))
