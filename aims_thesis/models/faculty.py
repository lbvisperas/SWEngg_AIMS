from odoo import models, fields


class Faculty(models.Model):
    _inherit = "student.faculty"
    student_thesis = fields.One2many('student.thesis', 'student_id', string='Faculty_Thesis')
    student_thesis_progress = fields.One2many('student.thesis.progress', 'student_id', string='Faculty_Thesis_Progress')
    student_thesis_defense = fields.One2many('student.thesis.defense', 'student_id', string='Faculty_Thesis_Defense')

