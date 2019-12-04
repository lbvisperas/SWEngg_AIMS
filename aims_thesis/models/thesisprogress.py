# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ThesisProgress(models.Model):
    _name = 'student.thesis.progress'
    _description = 'Student Thesis Progress'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def action_request(self):
        for rec in self:
            rec.state = 'submitted'

    def action_accept(self):
        for rec in self:
            rec.state = 'progress'

    def action_approval(self):
        for rec in self:
            rec.state = 'approve'

    def action_refuse(self):
        for rec in self:
            rec.state = 'refuse'

    def action_reset(self):
        for rec in self:
            rec.state = 'draft'

    @api.onchange('student_no')
    def onchange_student(self, context=None):
        for rec in self:
            rec.student_id = rec.student_no.student_no
            rec.first_name = rec.student_no.name
            rec.middle_name = rec.student_no.middle_name
            rec.last_name = rec.student_no.last_name
            rec.level = rec.student_no.education_level
            rec.program = rec.student_no.category_id.name
            rec.gpa = rec.student_no.gpa
            rec.email = rec.student_no.email
            rec.mobile = rec.student_no.mobile

    @api.onchange('advisor')
    def onchange_advisor(self, context=None):
        return 0

    @api.onchange('chairman')
    def onchange_chairman(self, context=None):
        for rec in self:
            rec.chairman_position = rec.chairman.faculty_role

    @api.onchange('chairman')
    def onchange_member(self, context=None):
        for rec in self:
            rec.member_position = rec.member.faculty_role

    @api.onchange('chairman')
    def onchange_advisor_member(self, context=None):
        for rec in self:
            rec.advisor_member_position = rec.advisor_member.faculty_role

    # Inherited from student_academic
    student_no = fields.Many2one('student.student', 'Student', required=True, track_visibility='onchange')

    first_name = fields.Char(string='First name')
    middle_name = fields.Char(string='Middle name')
    last_name = fields.Char(string='Last name')
    student_id = fields.Integer(string='Student ID')

    level = fields.Char(string='Education level')
    program = fields.Char(string='Program')
    department = fields.Char(string='Department')
    address = fields.Char(string='Address')
    mobile = fields.Integer(string='Mobile')
    email = fields.Char(string='Email')
    gpa = fields.Float(string='GPA')

    proposal_title = fields.Char(string='Proposal thesis title')
    # semester = fields.Char(string='Semester')

    date_proposal = fields.Date('Approved proposal on')
    datetime_progress = fields.Datetime('Date and time')
    room = fields.Char("Room no.")
    building = fields.Char("Building")

    # Inherited from student.faculty
    advisor = fields.Many2one('student.faculty', 'Advisor', require=True, track_visibility='onchange')
    co_advisor_first = fields.Many2one('student.faculty', 'Co-Advisor', require=True, track_visibility='onchange')
    co_advisor_second = fields.Many2one('student.faculty', 'Co-Advisor', require=True, track_visibility='onchange')

    # Inherited from student.faculty
    chairman = fields.Many2one('student.faculty', 'Chairman', require=True, track_visibility='onchange')
    chairman_position = fields.Char(string='Position')
    chairman_office = fields.Char(string='Office')
    chairman_mobile = fields.Integer(string='Mobile')

    member = fields.Many2one('student.faculty', 'Member', require=True, track_visibility='onchange')
    member_position = fields.Char(string='Position')
    member_office = fields.Char(string='Office')
    member_mobile = fields.Integer(string='Mobile')

    advisor_member = fields.Many2one('student.faculty', 'Advisor member', require=True, track_visibility='onchange')
    advisor_member_position = fields.Char(string='Position')
    advisor_member_office = fields.Char(string='Office')
    advisor_member_mobile = fields.Integer(string='Mobile')

    state = fields.Selection(
        [('draft', 'Draft'), ('submitted', 'Submitted'), ('progress', 'In Progress'), ('approve', 'Approved'),
         ('refuse', 'Refused')], string='Status', readonly='True', default='draft')
