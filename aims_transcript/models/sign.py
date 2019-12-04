# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Signature(models.Model):
    _name = "student.sign"
    _description = "Digital Signature"

    name = fields.Char(string="Name")
    sign = fields.Binary(string="Digital Signature")