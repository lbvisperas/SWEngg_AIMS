# -*- coding: utf-8 -*-


from odoo import models, fields


class StudentDepartment(models.Model):
    _name = "student.department"
    _description = "TGGS Department"

    name = fields.Char('Name', size=256, required=True)
    code = fields.Char('Code', size=16, required=True)

    _sql_constraints = [
        ('unique_department_code',
         'unique(code)', 'Code should be unique per department!')]
