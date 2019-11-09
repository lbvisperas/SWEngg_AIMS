# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentFaculty(models.Model):
    _name = "student.faculty"
    _description = "TGGS Faculty"
    _inherit = "mail.thread"
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one('res.partner', 'Partner',
                                 required=True, ondelete="cascade")
    middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128, required=True)
    birth_date = fields.Date('Birth Date', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], 'Gender', required=True)
    nationality = fields.Many2one('res.country', 'Nationality')
    emergency_contact = fields.Many2one(
        'res.partner', 'Emergency Contact')
    login = fields.Char(
        'Login', related='partner_id.user_id.login', readonly=1)
    last_login = fields.Datetime('Latest Connection', readonly=1,
                                 related='partner_id.user_id.login_date')
    emp_id = fields.Many2one('hr.employee', 'TGGS Faculty User')

    # Course and Department Based
    faculty_course_id = fields.Many2one('student.course', 'Course')
    faculty_department = fields.Many2one('student.course', 'Department')
    faculty_role = fields.Selection([
        ('coordinator', 'Coordinator'),
        ('lecturer', 'Lecturer'),
        ('lecturer and researcher', 'Lecturer and Researcher'),
        ('research assistant', 'Research Assistant'),
    ], 'Faculty Role')
    faculty_subject_ids = fields.Many2many('student.subject', string='Subject(s)',
                                           track_visibility='onchange')

    @api.multi
    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))

    @api.multi
    def create_employee(self):
        for record in self:
            vals = {
                'name': record.name + ' ' + (record.middle_name or '') +
                ' ' + record.last_name,
                'country_id': record.nationality.id,
                'gender': record.gender,
                'address_home_id': record.partner_id.id
            }
            emp_id = self.env['hr.employee'].create(vals)
            record.write({'emp_id': emp_id.id})
            record.partner_id.write({'supplier': True, 'employee': True})

    #@api.model
    #def get_import_templates(self):
     #   return [{
     #       'label': _('Import Template for Faculties'),
     #       'template': '/student_academic/static/xls/student_faculty.xls'
     #   }]