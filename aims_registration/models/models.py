# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Registration(models.Model):
    _name = 'registration.new'
    _description = "Registration"

    title = fields.Many2one('res.partner.title', 'Title')
    image = fields.Binary('Image')
    first_name = fields.Char(string='FirstName')
    last_name = fields.Char(string='LastName')
    student_ID = fields.Integer(string='Student ID')
    registration_NO = fields.Integer(string='Registration No.',
                                     default=lambda self: self.env['ir.sequence'].next_by_code('registration.new'))
    registration_date = fields.Datetime(
        'Registration Date',
        default=lambda self: fields.Datetime.now())
    course = fields.Selection([('SSE', 'Software Systems Engineering'), ('SGE', 'Smart Grids Engineering'),
                               ('EPE', 'Electrical Power Engineering')]
                              , string='Course')
    subject = fields.Selection([('DM', 'Design Methodology'), ('SWE', 'Software Engineering'), ('MV', 'Machine Vision')]
                               , string='Subject')
    batch = fields.Selection([('18_2', 'TGGS_2018_Aug'), ('19_1', 'TGGS_2019_Jan'), ('19_2', 'TGGS_2019_Aug')]
                             , string='Batch')
    state = fields.Selection([('draft', 'Draft'), ('submit', 'Submitted'), ('confirm', 'Confirmed'),
                              ('refuse', 'Refused'), ], required=True, default='draft')

    @api.mlti
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
