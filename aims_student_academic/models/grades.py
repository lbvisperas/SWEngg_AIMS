
import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentGrades(models.Model):
    _name = "student.grades"
    _inherit = "mail.thread"
    _description = "Exam"

    course_id = fields.Many2one(
        'student.course', store=True,readonly=True)
    batch_id = fields.Many2one(
        'student.batch', 'Batch / Semester',store=True,readonly=True)
    subject_id = fields.Many2one('student.subject', 'Subject', required=True)
    faculty_id = fields.Many2one(
        'student.faculty', 'Teaching Faculty', default=lambda self: self.env[
            'student.faculty'].search([('user_id', '=', self.env.uid)]),
        required=True)
    #put subject code here
    #exam_code = fields.Char('Exam Code', size=16, required=True)
    students_line = fields.One2many(
        'student.grades.students', 'exam_id', 'Students', readonly=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('result_updated', 'Result Updated'), ('done', 'Done'),
         ('submitted', 'Submitted'), ('approved', 'Approved')], 'State',
        readonly=True, default='draft', track_visibility='onchange')
    note = fields.Text('Note')
    responsible_id = fields.Many2many('student.faculty', string='Responsible')
    name = fields.Char('Exam', size=256, required=True)
    total_marks = fields.Integer('Total Marks', required=True)
    min_marks = fields.Integer('Passing Marks', required=True)

    _sql_constraints = [
        ('unique_exam_code',
         'unique(exam_code)', 'Code should be unique per exam!')]

    @api.constrains('total_marks', 'min_marks')
    def _check_marks(self):
        if self.total_marks <= 0.0 or self.min_marks <= 0.0:
            raise ValidationError(_('Enter proper marks!'))
        if self.min_marks > self.total_marks:
            raise ValidationError(_(
                "Passing Marks can't be greater than Total Marks"))

    @api.constrains('start_time', 'end_time')
    def _check_date_time(self):
        session_start = datetime.datetime.combine(
            fields.Date.from_string(self.session_id.start_date),
            datetime.time.min)
        session_end = datetime.datetime.combine(
            fields.Date.from_string(self.session_id.end_date),
            datetime.time.max)
        start_time = fields.Datetime.from_string(self.start_time)
        end_time = fields.Datetime.from_string(self.end_time)
        if start_time > end_time:
            raise ValidationError(_('End Time cannot be set \
            before Start Time.'))
        elif start_time < session_start or start_time > session_end or \
                end_time < session_start or end_time > session_end:
            raise ValidationError(
                _('Exam Time should in between Exam Session Dates.'))

    @api.multi
    def act_result_updated(self):
        self.state = 'result_updated'

    @api.multi
    def act_done(self):
        self.state = 'done'

    @api.multi
    def act_draft(self):
        self.state = 'draft'

    @api.multi
    def act_cancel(self):
        self.state = 'cancel'