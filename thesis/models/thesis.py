# -*- coding: utf-8 -*-

from odoo import models, fields

class ThesisProposal(models.Model):
    _name = 'thesisproposal'

    first_name = fields.Char(string='FirstName')
    last_name = fields.Char(string='LastName')
    student_ID = fields.Integer(string='Student ID')
    level = fields.Selection([('master', 'Master'), ('doctoral', 'Doctoral')], string='Education Level')
    program = fields.Selection([('sse', 'Software Systems Engineering'), ('sge', 'Smart Grid Engineering')], string='Program')
    department = fields.Selection([('esse', 'Electrical Software Systems Engineering'), ('me', 'Mechanical Engineering')], string='Department')
    address = fields.Char(string='Address')
    mobile = fields.Integer(string='Mobile')
    email = fields.Char(string='Email')
    proposal_title = fields.Char(string='Proposal Thesis Title')
    semester = fields.Char(string='Semester')
    gpa = fields.Float(string='GPA')
    state = fields.Selection([('draft','Draft'),('progress','In Progress'),('approval','Approval')], string='Status', readonly='True', default='draft')

