from odoo import models, fields


class StudentStudent(models.Model):
    _inherit = "student.student"
    student_internship = fields.One2many('student.internship', 'student_id', string='Student_Internship')