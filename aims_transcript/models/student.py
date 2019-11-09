# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'student'

    image = fields.Boolean(string='image')
    title = fields.Char(string='Tittle')
    first_name = fields.Char(string='FirstName')
    middle_name = fields.Char(string='MiddleName')
    last_name = fields.Char(string='LastName')
    student_ID = fields.Char(string='Student ID')
    level = fields.Selection([('master', 'Master'), ('doctoral', 'Doctoral')], string='Education Level')
    program = fields.Selection([('sse', 'Software Systems Engineering'), ('sge', 'Smart Grid Engineering'), ('epe', 'Electrical Power and Energy Engineering'), ('cse', 'Communication and Smart System Engineering')], string='Program')
    department = fields.Selection([('esse', 'Electrical Software Systems Engineering'), ('me', 'Mechanical Engineering'), ('cpe', 'Chemical and Process Engineering')], string='Department')
    address = fields.Char(string='Address')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    semester = fields.Char(string='Semester')
    gpa = fields.Float(string='GPA')