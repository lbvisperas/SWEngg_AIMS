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
    country_birth = fields.Many2one('res.country', 'Country of Birth')
    nationality = fields.Many2one('res.country', 'Nationality', required=True)
    nat_check = fields.Boolean(compute='_get_value')
    #citizen_id = fields.Char('Citizen ID', size=128)
    height = fields.Integer(string="Height (cm)", size=64)
    weight = fields.Integer(string="Weight (kg)", size=64)
    status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced')
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
    ], string='Blood Group', default='A+', track_visibility='onchange')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')

    # Mobile and Email are actually inherited from res.partner; and are / will be equal <=>
    mobile = fields.Char('Mobile', size=10)
    email = fields.Char('Email', size=128, track_visibility='always')
    emergency_contact = fields.Many2one('res.partner', 'Emergency Contact', required=True)
    #mother_name = fields.Many2one('res.partner', 'Mother Name', required=True)
    #father_name = fields.Many2one('res.partner', 'Father Name', required=True)
    partner_id = fields.Many2one('res.partner', 'Contact Info', ondelete="cascade", required=True)

    # PASSPORT INFORMATION
    passport_number = fields.Char(string='Passport Number', track_visibility='always', size=128, required=True)
    passport_issue = fields.Date('Passport Issuance Date')
    passport_expire = fields.Date('Passport Expiry Date')
    visa_number = fields.Char('Visa Number', size=20, required=True)
    visa_issue = fields.Date('Visa Issuance Date')
    visa_expire = fields.Date('Visa Expiry Date')

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
    category_id = fields.Many2one('student.category', 'Scholarship Category')
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
         '[ERROR] Mobile Number must be unique per student!'),
        ('unique_email',
         'unique(email)',
         '[ERROR] Email must be unique per student!'),
        ('unique_student_no',
         'unique(student_no)',
         '[ERROR] Student Number must be unique per student!'),
    ]

    # Student Number Check
    @api.multi
    @api.constrains('student_no')
    def _check_student_no(self):
        for record in self:
            if record.student_no:
                if len(record.student_no) != 13:
                    raise ValidationError(
                        "[ERROR] You have not entered your full user ID by entering% d digits, please enter 13 digits" % len(
                            record.student_no))
                index = 0
                listData = list(record.student_no)
                checkSum = 0  # Results
                while index < 12:
                    checkSum += int(listData[index]) * (13 - index)
                    index += 1
                digit13 = checkSum % 11
                if digit13 != int(listData[12]):
                    self.nat_check = False

    # ensures that weight and height are not zero values
    @api.multi
    @api.constrains('weight', 'height')
    def check_physical(self):
        for record in self:
            if record.weight == 0:
                raise ValidationError(_(
                    "[ERROR] Weight cannot be a zero value"))
            if record.height == 0:
                raise ValidationError(_(
                    "[ERROR] Height cannot be a zero value"))

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

    #ensures that passport and visa number are not zero values

    @api.multi
    @api.constrains('passport_number')
    def passport_check(self):
        for record in self:
            if len(record.passport_number) > 128:
                raise ValidationError(_(
                    "[ERROR] Passport Number cannot be greater than 128 characters"))
            if len(record.passport_number) < 1:
                raise ValidationError(_(
                    "[ERROR] Passport Number cannot be less than 1 character"))

    @api.multi
    @api.constrains('visa_number')
    def visa_check(self):
        for record in self:
            if len(record.visa_number) > 20:
                raise ValidationError(_(
                    "[ERROR] Visa Number cannot greater than 20 characters"))
            if len(record.visa_number) < 1:
                raise ValidationError(_(
                    "[ERROR] Visa Number cannot be less than 1 character"))


    @api.multi
    @api.onchange('nationality')
    def _get_value(self):
        if self.nationality.name == "Thailand":
            self.nat_check = True
        else:
            self.nat_check = False

    @api.multi
    @api.constrains('birth_date')
    def check_birth_date(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "[ERROR] Birth Date cannot be greater than current date!"))

    @api.multi
    @api.constrains('mobile')
    def check_mobile(self):
        for record in self:
            if record.mobile:
                if len(record.mobile) != 10:
                    raise ValidationError(_(
                        "[ERROR] Mobile number must be a 10 digit Thailand Number (e.g. 0656049400"))
                if record.mobile[0:1] != '0':
                    raise ValidationError(_(
                        "[ERROR] Mobile number must be a VALID 10 digit Thailand Number (e.g. 0656049400) %s" %str(record.mobile[0:1])))
                else:
                    record.partner_id.mobile = record.mobile
                    record.partner_id.email = record.email

    # Course Test Relationship <=> is course equivalent to parent
    @api.multi
    @api.onchange('student_course_id')
    def check_course_details(self):
        for record in self:
            if record.student_department:
                record.student_department = record.student_course_id.parent_id
            if record.course_detail_ids:
                record.course_detail_ids.course_id = record.student_course_id
                record.course_detail_ids.department = record.student_department

    @api.multi
    @api.onchange('student_course_id', 'first_name', 'last_name')
    def onchange_email(self):
        for record in self:
            if record.email:
                record.email = ((str(record.first_name)).lower() or '') + '.' + \
                               ((str(record.last_name[0])).lower() or '') + '-' \
                               + ((str(record.student_course_id.code)).lower() or '') + '2019@tggs.kmutnb.ac.th'
                record.partner_id.email = record.email
            if record.name:
                record.name = str(record.first_name) + ' ' + (str(record.middle_name[0]) or '') + ' ' + str(record.last_name)

    @api.multi
    @api.constrains('course_detail_ids')
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
                    'login': record.email,
                    'groups_id': user_group,
                })
                record.user_id = user_id
