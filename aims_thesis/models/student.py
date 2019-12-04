from odoo import models, fields


class StudentStudent(models.Model):
    _inherit = "student.student"
    student_thesis = fields.One2many('student.thesis', 'student_id', string='Student_Thesis')
    student_thesis_progress = fields.One2many('student.thesis.progress', 'student_id', string='Student_Thesis_Progress')
    student_thesis_defense = fields.One2many('student.thesis.defense', 'student_id', string='Student_Thesis_Defense')
    student_publication = fields.One2many('student.publication', 'student_id', string='Student_Publication')
