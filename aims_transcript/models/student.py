from odoo import models, fields


class StudentStudent(models.Model):
    _inherit = "student.student"
    student_transcript = fields.One2many('student.transcript', 'student_id', string='Student_Transcript')