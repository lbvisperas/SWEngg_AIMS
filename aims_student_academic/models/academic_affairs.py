# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentAffairs(models.Model):
    _name = "student.affairs"
    _description = "TGGS Faculty"
    _inherit = "mail.thread"
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one('res.partner', 'Partner',
                                 required=True, ondelete="cascade")
    first_name = fields.Char('First Name', size=128)
    middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128, required=True)
    affairs_role = fields.Selection([
        ('overall coordinator', 'Overall Coordinator'),
        ('thai coordinate', 'Thai Coordinator'),
        ('international coordinator', 'International Coordinator'),
        ('faculty coordinator', 'Faculty Coordinator'),
    ], 'Faculty Role')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], 'Gender', required=True)
    birth_date = fields.Date('Birth Date', required=True)
    last_login = fields.Datetime('Latest Connection', readonly=1,
                                 related='partner_id.user_id.login_date')
    emp_id = fields.Many2one('hr.employee', 'TGGS Academic Affairs User')
    emergency_contact = fields.Many2one(
        'res.partner', 'Emergency Contact')

    @api.multi
    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))

    @api.multi
    @api.onchange('last_name')
    def res_partner_name(self):
        for record in self:
            if record.last_name:
                record.name = str(record.first_name) + ' ' + str(record.middle_name[0]) + ' ' + str(record.last_name)

    @api.multi
    @api.constrains('first_name')
    def name_check(self):
        for record in self:
            if len(record.first_name) > 128:
                raise ValidationError(_(
                    "[ERROR] First Name cannot be greater than 128 characters"))
            if len(record.first_name) < 1:
                raise ValidationError(_(
                    "[ERROR] First Name cannot be less than 1 character"))

    @api.multi
    @api.constrains('last_name')
    def name_check(self):
        for record in self:
            if len(record.last_name) > 128:
                raise ValidationError(_(
                    "[ERROR] Last Name cannot be greater than 128 characters"))
            if len(record.last_name) < 1:
                raise ValidationError(_(
                    "[ERROR] Last Name cannot be less than 1 character"))

    @api.multi
    @api.constrains('middle_name')
    def name_check(self):
        for record in self:
            if len(record.middle_name) > 128:
                raise ValidationError(_(
                    "[ERROR] Middle Name cannot be greater than 128 characters"))
            if len(record.middle_name) < 1:
                raise ValidationError(_(
                    "[ERROR] Middle cannot be less than 1 character"))

    @api.multi
    def create_employee(self):
        for record in self:
            vals = {
                'name': record.name + ' ' + (record.middle_name or '') +
                ' ' + record.last_name,
                'gender': record.gender,
                'address_home_id': record.partner_id.id
            }
            emp_id = self.env['hr.employee'].create(vals)
            record.write({'emp_id': emp_id.id})
            record.partner_id.write({'supplier': True, 'employee': True})

    @api.multi
    def create_academic_user(self):
        user_group = self.env.ref("aims_student_academic.group_student_back_office") or False
        users_res = self.env['res.users']
        for record in self:
            if not record.user_id:
                user_id = users_res.create({
                    'name': str(record.first_name) + ' ' + (str(record.middle_name[0]) or '') + ' ' + str(
                        record.last_name),
                    'partner_id': record.partner_id.id,
                    'login': record.email or (record.first_name + ' ' + record.last_name),
                    'groups_id': user_group,
                })
                record.user_id = user_id

    #@api.model
    #def get_import_templates(self):
     #   return [{
     #       'label': _('Import Template for Faculties'),
     #       'template': '/aims_student_academic/static/xls/student_faculty.xls'
     #   }]