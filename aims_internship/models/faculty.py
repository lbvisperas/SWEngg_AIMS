from odoo import models, fields


class StudentFaculty(models.Model):
    _inherit = "student.faculty"
    student_internship = fields.One2many('student.internship', 'student_id', string='Student_Internship')