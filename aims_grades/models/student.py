# -*- coding: utf-8 -*-

from odoo import models, fields


class StudentStudent(models.Model):
    _inherit = "student.student"
    allocation_ids = fields.Many2many('student.section', string='Assignment(s)')
    grades_ids = fields.Many2many('student.list.grades', string='Assignment(s)')
