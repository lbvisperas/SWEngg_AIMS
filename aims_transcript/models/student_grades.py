from odoo import fields, models, api


class StudentGrade(models.Model):
    _name = "student.sgrades"
    _rec_name = "subject_name"
    _description = "Student Grades"

    subject_id = fields.Many2one('student.subject', 'Subject', required=True,
                                 track_visibility='onchange')
    subject_name = fields.Char(string="Subject")
    code = fields.Char(string="Code")
    subject_type = fields.Char(string="Type")
    grade = fields.Float(string="Grade")
    states = fields.Selection([
        ('show', "Show"),
        ('hide', "Hide")
    ], default="show")

    @api.onchange('subject_id')
    def onchange_subject(self, context=None):
        for record in self:
            record.subject_name = record.subject_id.name
            record.code = record.subject_id.code
            record.subject_type = record.subject_id.subject_type
            record.states = "hide"
