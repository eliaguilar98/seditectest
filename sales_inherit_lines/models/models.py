# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sales_inherit_lines(models.Model):
     _name = 'sales_inherit_lines.sales_inherit_lines'
     _description = 'sales_inherit_lines.sales_inherit_lines'
     _inherit = "sale.order.line"

     margin_percent = fields.Float(
         readonly=False
     )


