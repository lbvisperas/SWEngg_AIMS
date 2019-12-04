# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import pdfrw
import os.path
from os import path
import base64


class StudentGrade(models.Model):
    _name = "student.sgrades"
    _rec_name = "subject_name"
    _description = "Student Grades"

    subject_id = fields.Many2one('student.subject', 'Subject', required=True,
                                 track_visibility='onchange')
    subject_name = fields.Char(string="Subject")
    code = fields.Char(string="Code")
    subject_type = fields.Char(string="Type")
    grade = fields.Float(string="Grade")
    states = fields.Selection([
        ('show', "Show"),
        ('hide', "Hide")
    ], default="show")

    @api.onchange('subject_id')
    def onchange_subject(self, context=None):
        for record in self:
            record.subject_name = record.subject_id.name
            record.code = record.subject_id.code
            record.subject_type = record.subject_id.subject_type
            record.states = "hide"


class Grade(models.Model):
    _name = "student.grades"
    _rec_name = "first_name"
    _description = "Grades"

    # inf_student
    student_no = fields.Many2one('student.student', 'Student', required=True,
                                 track_visibility='onchange')
    student_id = fields.Char('Student Number')
    full_name = fields.Char(compute='concat_name', string="Full Name", store=True)
    first_name = fields.Char(string='First Name')
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')

    study_school = fields.Char("School")
    study_field = fields.Char("Branch")
    program = fields.Many2one('student.category', 'Program', track_visibility='onchange')
    student_course_id = fields.Many2one('student.student.course', 'Student Course',
                                        track_visibility='onchange')
    student_course = fields.Char(string="Course")
    semester = fields.Char(string='Semester')
    education_level = fields.Char(string='Level of Education Acquired')
    gpa = fields.Float(string="GPA", default="0")

    student_grades_id = fields.Many2many('student.sgrades', string='Student Grades', required=True)
    report_name = fields.Char(string="Report", compute='rename_file')
    report_transcript = fields.Binary(string='Download Transcript')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('request', 'Request')
    ], string='Request Status', required=True, default='draft')

    @api.depends('first_name', 'middle_name', 'last_name')
    def concat_name(self):
        for record in self:
            record.full_name = (record.first_name or '') + ' ' + (record.middle_name or '') + ' ' + (
                    record.last_name or '')

    @api.onchange('student_no')
    def onchange_student_course(self, context=None):
        for record in self:
            record.student_id = record.student_no.student_no
            record.first_name = record.student_no.name
            record.middle_name = record.student_no.middle_name
            record.last_name = record.student_no.last_name
            record.education_level = record.student_no.education_level
            record.program = record.student_no.category_id
            record.study_field = record.student_no.study_field
            record.study_school = record.student_no.study_school

    @api.onchange('student_course_id')
    def onchange_student(self, context=None):
        for record in self:
            record.student_course = record.student_course_id.course_id.name
            record.semester = record.student_course_id.batch_id.semester

    @api.onchange('student_grades_id')
    def calculate_gpa(self):
        total = 0
        for record in self:
            if record.student_grades_id:
                for subject in record.student_grades_id:
                    total += subject.grade
                record.gpa = total / len(record.student_grades_id)
            else:
                record.gpa = 0

    @api.multi
    def action_reset_draft(self):
        for record in self:
            record.state = 'draft'

    @api.multi
    def action_submitted(self):
        for record in self:
            record.state = 'request'
            now = datetime.datetime.now()
            current_dir = os.path.dirname(os.path.abspath(__file__))
            transcript_path = os.path.join(current_dir, 'transcript_form.pdf')
            transcript_path_output = os.path.join(current_dir, 'transcript_output.pdf')
            data = {
                'date': now.day,
                'month': now.month,
                'year': now.year,
                'full_name': record.full_name,
                'student_id': record.student_id,
                'education_level': False,
                'school': record.study_school,
                'mobile': record.student_no.mobile,
                'email': record.student_no.email,
            }

            template_pdf = pdfrw.PdfReader(transcript_path)
            template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
            annotations = template_pdf.pages[0]['/Annots']
            for annotation in annotations:
                if annotation['/Subtype'] == '/Widget':
                    if annotation['/T']:
                        key = annotation['/T'][1:-1]
                        if key in data.keys():
                            annotation.update(pdfrw.PdfDict(V='{}'.format(data[key])))
            pdfrw.PdfWriter().write(transcript_path_output, template_pdf)
            self.report_transcript = base64.b64encode(open(transcript_path_output, "rb").read())

    @api.one
    def rename_file(self):
        for record in self:
            if record.state == "request":
                record.report_name = 'Transcript.pdf'
