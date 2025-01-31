# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sales_inherit_lines(models.Model):
     _inherit = "sale.order.line"

     margin_percent = fields.Float(
         readonly=False
     )


