from odoo import models, fields


class StudentStudent(models.Model):
    _inherit = "student.subject"
    student_transcript = fields.One2many('student.internship', 'student_id', string='Student_Transcript')
