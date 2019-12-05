# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentCategory(models.Model):
    _name = "student.category"
    _description = "TGGS Scholarships"

    name = fields.Char('Name', size=128, required=True)
    description = fields.Text('Description', size=256, required=True)

    _sql_constraints = [
        ('unique_category_name',
         'unique(name)', 'Program name should be unique per program category!')]

    @api.multi
    @api.constrains('name')
    def name_check(self):
        for record in self:
            if len(record.name) > 128:
                raise ValidationError(_(
                    "[ERROR] Name cannot be greater than 128 characters"))
            if len(record.name) < 1:
                raise ValidationError(_(
                    "[ERROR] Name cannot be less than 1 character"))

    @api.multi
    @api.constrains('description')
    def desc_check(self):
        for record in self:
            if len(record.description) > 256:
                raise ValidationError(_(
                    "[ERROR] Name cannot be greater than 256 characters"))
            if len(record.description) < 256:
                raise ValidationError(_(
                    "[ERROR] Name cannot be less than 1 character"))