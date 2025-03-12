# -*- coding: utf-8 -*-

from odoo import models, fields, api


class margin_inherit(models.Model):
    _inherit = "sale.order.line"

    margin_percent = fields.Float(
        readonly = False,
    )

    #price_unit = fields.Float(
     #   compute = '_compute_price_unit'
    #)

    #@api.onchange('margin_percent')
    #def _compute_price_unit(self):
     #   for line in self:
      #      line.price_unit = line.purchase_price / (1 - line.margin_percent)






