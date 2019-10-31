# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentStudentCourse(models.Model):
    _name = "student.student.course"
    _description = "Student Course Details"

    student_id = fields.Many2one('student.student', 'Student Number', ondelete="cascade")
    course_id = fields.Many2one('student.course', 'Course', required=True)
    batch_id = fields.Many2one('student.batch', 'Batch', required=True)
    department = fields.Many2one('student.course', 'Department', required=True)
    subject_ids = fields.Many2many('student.subject', string='Subjects')

    sql_constraints = [
        ('unique_name_department_id',
         'unique(department,batch_id,student_id)',
         'Department & Student must be unique per Batch!'),
        #('unique_name_department_course_id',
        # 'unique(department,course_id)',
         #'Department must be unique per Batch!'),
        ('unique_name_department_student_id',
         'unique(student_id,course_id,batch_id)',
         'Student must be unique per Batch!'),
    ]


class StudentStudent(models.Model):
    _name = "student.student"
    _description = "Student"
    _inherit = "mail.thread"
    _inherits = {"res.partner": "partner_id"}

    # BASIC STUDENT INFORMATION
    student_no = fields.Char('Student Number', size=20, required=True)
    middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128)
    birth_date = fields.Date('Birth Date')
    country_birth = fields.Many2one('res.country','Country of Birth')
    nationality = fields.Many2one('res.country', 'Nationality', required=True)
    nat_check = fields.Boolean(compute='_get_value')
    # religion = fields.Many2one('religion.religion', string="Religion")
    height = fields.Integer(string="Height (cm)")
    weight = fields.Integer(string="Weight (kg)")
    status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], string='Marital Status', required=True, default='single')
    blood_group = fields.Selection([
        ('A+', 'A+ve'),
        ('B+', 'B+ve'),
        ('O+', 'O+ve'),
        ('AB+', 'AB+ve'),
        ('A-', 'A-ve'),
        ('B-', 'B-ve'),
        ('O-', 'O-ve'),
        ('AB-', 'AB-ve')
    ], string='Blood Group', required=True, default='A+', track_visibility='onchange')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', required=True, default='male', track_visibility='onchange')
    mobile = fields.Char('Mobile', required=True,)
    email = fields.Char('Email', required=True,)
    emergency_contact = fields.Many2one('res.partner', 'Emergency Contact')
    passport_number = fields.Char(string='Passport Number', track_visibility='always', required=True)
    passport_issue = fields.Date('Passport Issuance Date')
    passport_expire = fields.Date('Passport Expiry Date')
    visa_number = fields.Char('Visa Number', size=64, required=True)
    visa_issue = fields.Date('Visa Issuance Date')
    visa_expire = fields.Date('Visa Expiry Date')
    # partner_id = fields.Many2one('res.partner', 'Partner', required=True, ondelete="cascade")

    # BASIC FAMILY INFORMATION
    parent_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], string='Marital Status', default='single')
    fin_support = fields.Selection([
        ('parents', 'Parents'),
        ('relative', 'Relative'),
        ('company', 'Company'),
        ('scholarship', 'Scholarship'),
        ('self', 'Self'),
    ], string='Received Financial Support From', default='scholarship')
    father_name = fields.Char(string="Father's Name")
    mother_name = fields.Char(string="Mother's Name")

    # EDUCATIONAL INFORMATION
    category_id = fields.Many2one('student.category', 'Category')
    # student.student.course table
    course_detail_ids = fields.One2many('student.student.course', 'student_id',
                                        'Course Details',
                                        track_visibility='onchange')
    education_level = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctoral', 'Doctoral'),
        ('other', 'Other'),
    ], 'Level of Education Acquired', default='master')
    gpa = fields.Integer(string="Cumulative Grade Point Average")
    study_field = fields.Char("Branch", default='Bachelor of Engineering in Mechanical Engineering', required=True)
    study_school = fields.Char("School", default='King Mongkuts University of Technology', required=True)

    # LOGIN STATUS CHECK
    login = fields.Char(
        'Login', related='partner_id.user_id.login', readonly=1)
    last_login = fields.Datetime('Latest Connection', readonly=1,
                                 related='partner_id.user_id.login_date')
    _sql_constraints = [(
        'unique_student_no',
        'unique(student_no)',
        'Student Number must be unique per student!'
    )]

    @api.multi
    @api.onchange('nationality')
    def _get_value(self):
        if self.nationality.name == "Thailand":
            self.nat_check = True
        else:
            self.nat_check = False


    # Insert Thai Student Check
    @api.multi
    @api.onchange('nationality')
    def _get_value(self):
        if self.nationality.name == "Thailand":
            self.nat_check = True
        else:
            self.nat_check = False

    @api.multi
    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))

    #@api.model
    #def get_import_templates(self):
    #    return [{
    #        'label': _('Import Template for Students'),
    #        'template': '/school/static/xls/tggs_student.xls'
    #    }]

    @api.multi
    def create_student_user(self):
        user_group = self.env.ref("openeducat_core.group_op_student") or False
        users_res = self.env['res.users']
        for record in self:
            if not record.user_id:
                user_id = users_res.create({
                    'name': record.name,
                    'partner_id': record.partner_id.id,
                    'login': record.email,
                    'groups_id': user_group,
                })
                record.user_id = user_id
