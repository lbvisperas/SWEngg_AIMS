# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Grade(models.Model):
    _name = 'grades'
    _rec_name = 'student_name'

    # image = fields.Boolean(string='image')
    # title = fields.Char(string='Tittle')
    student_name = fields.Char(string='Student Name', related='student_ID.student_name')
    student_ID = fields.Char(string='Student ID',default=lambda self:'New')
    level = fields.Selection([('master', 'Master'), ('doctoral', 'Doctoral')], string='Education Level')
    program = fields.Selection([('sse', 'Software Systems Engineering'), ('sge', 'Smart Grid Engineering'), ('epe', 'Electrical Power and Energy Engineering'), ('cse', 'Communication and Smart System Engineering')], string='Program')
    department = fields.Selection([('esse', 'Electrical Software Systems Engineering'), ('me', 'Mechanical Engineering'), ('cpe', 'Chemical and Process Engineering')], string='Department')
    semester = fields.Char(string='Semester')
    subject = fields.Selection([('com','Computer Architect'),('alg','Efficient Algorithm'),('data','Data Management'),('sof','Advance Software'),('de','Design Method'),('co','Communication Protocol')])
    grade = fields.Char(string='Grade')
    state = fields.Selection([('draft', 'Draft'), ('submit', 'Submitted'), ('confirm', 'Confirmed'),
                              ('refuse', 'Refused'), ], required=True, default='draft')

    @api.multi
    def btn_submit(self):
        for rec in self:
            rec.write({'state': 'submit'})

    @api.multi
    def btn_confirm(self):
        for rec in self:
            rec.write({'state': 'confirm'})

    @api.multi
    def btn_refuse(self):
        for rec in self:
            rec.state = 'refuse'