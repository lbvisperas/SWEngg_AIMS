# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Publication(models.Model):
    _name = 'student.publication'
    _description = 'Student Publication'
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

    # Inherited from student_academic
    student_no = fields.Many2one('student.student', 'Student', required=True, track_visibility='onchange')

    first_name = fields.Char(string='First Name')
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')
    student_id = fields.Integer(string='Student ID')

    level = fields.Char(string='Education Level')
    program = fields.Char(string='Program')
    department = fields.Char(string='Department')
    address = fields.Char(string='Address')
    mobile = fields.Integer(string='Mobile')
    email = fields.Char(string='Email')
    gpa = fields.Float(string='GPA')

    # Publication infomation
    title = fields.Char(string='Title')
    author = fields.Char(string='Author')
    name = fields.Char(string='Conference/Journal name')
    date = fields.Date('Date')
    venue = fields.Char(string='Venue')
    citation = fields.Char(string='Citation')
    database = fields.Char(string='Database')

    state = fields.Selection(
        [('draft', 'Draft'), ('submitted', 'Submitted'), ('progress', 'In Progress'), ('approve', 'Approved'),
         ('refuse', 'Refused')], string='Status', readonly='True', default='draft')
