# -*- coding: utf-8 -*-

from odoo import models, fields


class StudentCategory(models.Model):
    _name = "student.category"
    _description = "TGGS Programs"

    name = fields.Char('Name', size=256, required=True)
    description = fields.Text('Description')

    _sql_constraints = [
        ('unique_category_name',
         'unique(name)', 'Program name should be unique per program category!')]
