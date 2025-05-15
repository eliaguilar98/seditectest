# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class crm_vendedor_restringido/(models.Model):
#     _name = 'crm_vendedor_restringido/.crm_vendedor_restringido/'
#     _description = 'crm_vendedor_restringido/.crm_vendedor_restringido/'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

