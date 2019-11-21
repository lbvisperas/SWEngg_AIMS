# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Grade(models.Model):
    _name = "student.grades"
    _rec_name = "first_name"
    _description = "Grades"

    # inf_student
    student_no = fields.Many2one('student.student', 'Student', required=True,
                                 track_visibility='onchange')
    student_id = fields.Char('Student Number')
    full_name = fields.Char(compute='concat_name', string="Full Name", store=True)
    first_name = fields.Char(string='First Name')
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')

    program = fields.Many2one('student.category', 'Program', track_visibility='onchange')
    student_course_id = fields.Many2one('student.course', 'Course', track_visibility='onchange')
    education_level = fields.Char(string='Level of Education Acquired')
    study_field = fields.Char("Branch")
    study_school = fields.Char("School")
    gpa = fields.Float(string="GPA", default="0")

    student_grades_id = fields.Many2many('student.sgrades', string='Student Grades')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('request', 'Request')
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
            record.program = record.student_no.category_id
            record.student_course_id = record.student_no.student_course_id
            record.study_field = record.student_no.study_field
            record.study_school = record.student_no.study_school

    @api.onchange('student_grades_id')
    def calculate_gpa(self):
        total = 0
        for record in self:
            if record.student_grades_id:
                for subject in record.student_grades_id:
                    total += subject.grade
                record.gpa = total / len(record.student_grades_id)
            else:
                record.gpa = 0

    @api.multi
    def action_reset_draft(self):
        for record in self:
            record.state = 'draft'

    @api.multi
    def action_submitted(self):
        for record in self:
            record.state = 'request'

