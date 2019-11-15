# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentStudentCourse(models.Model):
    _name = "student.student.course"
    _description = "TGGS Student Course"
    student_id = fields.Many2one('student.student', 'Student Number', ondelete="cascade")
    batch_id = fields.Many2one('student.batch', 'Batch', track_visibility='onchange')
    course_id = fields.Many2one('student.course', 'Course')
    department = fields.Many2one('student.course', 'Department')
    subject_ids = fields.Many2many('student.subject', string='Subjects')

    sql_constraints = [
        ('unique_name_student_id',
         'unique(student_id,course_id,batch_id)',
         'Student must be unique per Course / Batch!'),
    ]

class StudentStudent(models.Model):
    _name = "student.student"
    _description = "TGGS Student"
    _inherit = "mail.thread"
    _inherits = {"res.partner": "partner_id"}

    # BASIC STUDENT INFORMATION
    student_no = fields.Char('Student Number', size=13, required=True)
    first_name = fields.Char('First Name', size=128)
    middle_name = fields.Char('Middle Name', size=128, required=True)
    last_name = fields.Char('Last Name', size=128)
    birth_date = fields.Date('Birth Date')
    country_birth = fields.Many2one('res.country','Country of Birth')
    nationality = fields.Many2one('res.country', 'Nationality', required=True)
    nat_check = fields.Boolean(compute='_get_value')
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

    # get one specific class for mobile and contact information here
    mobile = fields.Char('Mobile')
    email = fields.Char('Email')
    emergency_contact = fields.Many2one('res.partner', 'Emergency Contact')

    # get one specific class for passport info ==> get this from Ather
    passport_number = fields.Char(string='Passport Number', track_visibility='always')
    passport_issue = fields.Date('Passport Issuance Date')
    passport_expire = fields.Date('Passport Expiry Date')
    visa_number = fields.Char('Visa Number', size=64)
    visa_issue = fields.Date('Visa Issuance Date')
    visa_expire = fields.Date('Visa Expiry Date')
    partner_id = fields.Many2one('res.partner', 'Partner', ondelete="cascade", required=True)

    # BASIC FAMILY INFORMATION
    parent_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], string='Parental Status', default='single')
    father_name = fields.Char(string="Father's Name")
    mother_name = fields.Char(string="Mother's Name")

    # PREVIOUS EDUCATIONAL INFORMATION
    education_level = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctoral', 'Doctoral'),
        ('other', 'Other'),
    ], 'Level of Education Acquired', default='master')
    gpa = fields.Integer(string="Cumulative Grade Point Average")
    study_field = fields.Char("Branch")
    study_school = fields.Char("School")

    # TGGS EDUCATIONAL INFORMATION
    category_id = fields.Many2one('student.category', 'Category')
    student_course_id = fields.Many2one('student.course', 'Course')
    student_batch_id = fields.Many2one('student.batch', 'Batch')
    student_department = fields.Many2one('student.course', 'Department')
    student_subject_ids = fields.Many2many('student.subject', string='Subject(s)',
                                           track_visibility='onchange')
    course_detail_ids = fields.One2many('student.student.course', 'student_id',
                                        'Admission Details',
                                        track_visibility='onchange')
    # LOGIN STATUS CHECK
    login = fields.Char(
        'Login', related='partner_id.user_id.login', readonly=1)
    last_login = fields.Datetime('Latest Connection', readonly=1,
                                 related='partner_id.user_id.login_date')
    _sql_constraints = [
        ('unique_mobile',
         'unique(mobile)',
         'Mobile Number must be unique per student!'),
        ('unique_email',
         'unique(email)',
         'Email must be unique per student!'),
        ('unique_student_no',
         'unique(student_no)',
         'Student Number must be unique per student!'),
    ]

    @api.multi
    @api.onchange('nationality')
    def _get_value(self):
        if self.nationality.name == "Thailand":
            self.nat_check = True
        else:
            self.nat_check = False

    @api.multi
    @api.onchange('last_name')
    def res_partner_name(self):
        for record in self:
            if record.last_name:
                record.name = str(record.first_name) + ' ' + str(record.middle_name[0]) + ' ' + str(record.last_name)

    # Student Number Check
    @api.multi
    @api.constrains('student_no')
    def _check_student_no(self):
        for record in self:
            if record.student_no:
                if len(record.student_no) != 13:
                    raise ValidationError(
                        "You have not entered your full user ID by entering% d digits, please enter 13 digits" % len(
                            record.student_no))
                index = 0  # Reference value index list Identification Card Information
                listData = list(record.student_no)  # listNational ID Card Information
                checkSum = 0  # Results
                while index < 12:
                    checkSum += int(listData[index]) * (13 - index)  # Combine the index values ​​with each index list * (13 - index) and combine them with checkSum.
                    index += 1  # Increase the index by 1
                digit13 = checkSum % 11  # checkSum divided by 11 take the numerator
                if digit13 != int(listData[12]):  # If the 13th digit value is equal to the 13th digit value entered, returns True.
                    self.nat_check = False

    @api.multi
    @api.constrains('birth_date')
    def check_birth_date(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "[ERROR] Birth Date cannot be greater than current date!"))

    # Course Test Relationship <=> is course equivalent to parent
    @api.multi
    @api.onchange('student_course_id')
    def check_course_details(self):
        for record in self:
            record.student_department = record.student_course_id.parent_id

    @api.multi
    @api.constrains('student_course_id')
    def constrain_course_details(self):
        for record in self:
            if record.course_detail_ids:
                if record.course_detail_ids.course_id != record.student_course_id:
                    raise ValidationError(_(
                        "[ERROR] Student Course enlisted in admissions should be "
                        "same as student course input previously!"))

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Students'),
            'template': '/aims_student_academic/static/xls/tggs_student.xls'
        }]

    # Code adapted from OpenEducat => need to integrate an environment for own module
    @api.multi
    def create_student_user(self):
        user_group = self.env.ref("aims_student_academic.group_student_student") or False
        users_res = self.env['res.users']
        for record in self:
            if not record.user_id:
                user_id = users_res.create({
                    'name': str(record.first_name) + ' ' + (str(record.middle_name[0]) or '') + ' ' + str(record.last_name),
                    'partner_id': record.partner_id.id,
                    'login': record.email or (record.first_name + ' ' + record.last_name),
                    'groups_id': user_group,
                })
                record.user_id = user_id
