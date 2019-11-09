from odoo import models, fields, api

class StudentCourse(models.Model):
    _name = "student.course"
    _inherit = "mail.thread"
    _description = "student course"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', size=16, required=True)
    parent_id = fields.Many2one('student.course', 'Department')
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('GPA', 'GPA'),
         ('CWA', 'CWA'), ('CCE', 'CCE')],
        'Evaluation Type', default="normal", required=True)
    subject_ids = fields.Many2many('student.subject', string='Subject(s)')
    coordinator = fields.Many2one('student.faculty', string='Coordinator')
    max_unit_load = fields.Float("Maximum Unit Load")
    min_unit_load = fields.Float("Minimum Unit Load")

    _sql_constraints = [
        ('unique_course_code',
         'unique(code)', 'Code should be unique per course!')]
