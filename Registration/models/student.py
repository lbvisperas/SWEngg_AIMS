from odoo import models, fields


class StudentStudent(models.Model):
    _inherit = "student.student"
    student_registration = fields.One2many('student.registration', 'student_id',
                                   string='Activity Log')