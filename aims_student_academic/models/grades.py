# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StudentListGrade(models.Model):
    _name = "student.list.grade"
    #_rec_name = "student_id"
    _description = "Students Enrolled"

    student_id = fields.Many2one('student.student', 'Student', required=True)
    marks = fields.Integer('Marks')
    note = fields.Text('Note')
    grades_id = fields.Many2one('student.grades', 'Grade', required=True, ondelete="cascade")
    course_id = fields.Many2one('student.course', 'Course', readonly=True)
    batch_id = fields.Many2one('student.batch', 'Batch', readonly=True)


class StudentGrades(models.Model):
    _name = "student.grades"
    _inherit = "mail.thread"
    _description = "grades"

    course_id = fields.Many2one('student.course', store=True)
    batch_id = fields.Many2one('student.batch', 'Batch / Semester', store=True)
    subject_id = fields.Many2one('student.subject', 'Subject', required=True)
    faculty_id = fields.Many2one('student.faculty', 'Teaching Faculty', required=True)
    name = fields.Char('Name', size=256, required=True)
    grade_code = fields.Char('Grade Code', size=256, required=True)
    students_line = fields.Many2many('student.list.grade', 'grades_id', 'Students')
    state = fields.Selection(
        [('draft', 'Draft'), ('result_updated', 'Result Updated'),('submitted', 'Submitted'),
         ('approved', 'Approved')], 'State',
        readonly=True, default='draft', track_visibility='onchange')
    note = fields.Text('Note')
    total_marks = fields.Integer('Total Marks', required=True)
    min_marks = fields.Integer('Passing Marks', required=True)
    reviewer = fields.Many2one('student.affairs', 'Reviewer', required=True)

    sql_constraints = [
        ('unique_grade_code',
         'unique(grade_code)', 'Code should be unique per grade!')]

    @api.constrains('total_marks', 'min_marks')
    def _check_marks(self):
        if self.total_marks <= 0.0 or self.min_marks <= 0.0:
            raise ValidationError(_('Enter proper marks!'))
        if self.min_marks > self.total_marks:
            raise ValidationError(_(
                "Passing Marks can't be greater than Total Marks"))

    #@api.multi
    #@api.onchange('semester')
    #def onchange_grades(self):
    #    for record in self:
            #record.name = str(record.batch_id.name) + str(record.subject_id.name)
            #record.grade_code = str(record.subject_id.name) + str(record.batch_id.semester)

    #@api.constrains('start_time', 'end_time')
    #def _check_date_time(self):
    #    session_start = datetime.datetime.combine(
    #        fields.Date.from_string(self.session_id.start_date),
    #        datetime.time.min)
    #    session_end = datetime.datetime.combine(
    #        fields.Date.from_string(self.session_id.end_date),
    #        datetime.time.max)
    #    start_time = fields.Datetime.from_string(self.start_time)
    #    end_time = fields.Datetime.from_string(self.end_time)
    #    if start_time > end_time:
    #        raise ValidationError(_('Grades cannot be set \
    #        before Start Time.'))
    #    elif start_time < session_start or start_time > session_end or \
    #            end_time < session_start or end_time > session_end:
    #        raise ValidationError(
    #            _('Exam Time should in between Exam Session Dates.'))

    @api.multi
    def act_result_updated(self):
        self.state = 'result_updated'

    @api.multi
    def act_submitted(self):
        self.state = 'submitted'

    @api.multi
    def act_draft(self):
        self.state = 'draft'

    @api.multi
    def act_approved(self):
        self.state = 'approved'