# -*- coding: utf-8 -*-

from odoo import models, fields


class StudentCategory(models.Model):
    _name = "student.category"
    _description = "TGGS Programs"

    name = fields.Char('Name', size=256, required=True)
    code = fields.Char('Code', size=16, required=True)

    _sql_constraints = [
        ('unique_category_code',
         'unique(code)', 'Code should be unique per program category!')]
