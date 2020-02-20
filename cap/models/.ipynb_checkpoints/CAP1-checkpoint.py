# -*- coding: utf-8 -*-

from odoo import models, fields


class CAP1(models.Model):
     _name = 'CAP1.CAP1'
     _description = 'CAP1.CAP1'

     label = fields.Char()
     monto = fields.Integer()
     monto2 = fields.Float(compute="_value_pc", store=True)
     detalle = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
