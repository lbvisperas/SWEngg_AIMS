# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Transcript(models.Model):
    _name = "student.transcript"
    _rec_name = "first_name"
    _inherit = ["mail.thread"]
    _description = "Student Transcript"

    # inf_student
    student_no = fields.Many2one('student.student', 'Student', required=True,
                                 track_visibility='onchange')  # based on student_academic
    student_id = fields.Char('Student Number')
    full_name = fields.Char(compute='concat_name', string="Full Name", store=True)
    first_name = fields.Char(string='First Name')
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')

    program = fields.Char(string='TGGS Programs')
    student_course_id = fields.Many2one('student.course', 'Course', track_visibility='onchange')
    education_level = fields.Char(string='Level of Education Acquired')
    semester = fields.Selection([
        ('first semester', 'First Semester'),
        ('second semester', 'Second Semester'),
        ('summer semester', 'Summer Semester'),
    ], 'Semester', default='first semester')
    subject = fields.Many2one('student.subject', 'Subject', track_visibility='onchange')
    evaluation_type = fields.Char(string='Evaluation Type')
    grade = fields.Integer(string="Grade")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('confirmed', 'Confirmed'),
        ('refused', 'Refused')
    ], string='Request Status', required=True, default='draft')

    @api.depends('first_name', 'middle_name', 'last_name')
    def concat_name(self):
        for record in self:
            record.full_name = (record.first_name or '') + ' ' + (record.middle_name or '') + ' ' + (
                        record.last_name or '')

    @api.onchange('student_no')
    def onchange_student(self, context=None):
        for record in self:
            record.student_id = record.student_no.student_no
            record.first_name = record.student_no.name
            record.middle_name = record.student_no.middle_name
            record.last_name = record.student_no.last_name
            record.education_level = record.student_no.education_level
            record.program = record.student_no.category_id.name
            record.student_course_id = record.student_no.student_course_id

    @api.onchange('student_course_id')
    def onchange_course(self, context=None):
        for record in self:
            record.evaluation_type = record.student_course_id.evaluation_type

    @api.multi
    def action_reset_draft(self):
        for record in self:
            record.state = 'draft'

    @api.multi
    def action_submitted(self):
        for record in self:
            record.state = 'submitted'

    @api.multi
    def action_confirmed(self):
        for record in self:
            record.state = 'confirmed'

    @api.multi
    def action_refused(self):
        for record in self:
            record.state = 'refused'



