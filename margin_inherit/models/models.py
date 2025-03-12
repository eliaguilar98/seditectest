# -*- coding: utf-8 -*-

from odoo import models, fields, api


class margin_inherit(models.Model):
    _inherit = "sale.order.line"

    margin_percent = fields.Float(
        readonly = False,
    )

    price_unit = fields.Float(
        compute = '_compute_price_unit'
    )

    @api.onchange('purchase_price','margin_percent')
    def _compute_price_unit(self):
        for line in self:
            if line.purchase_price != 0 and line.margin_percent != 0:
                line.price_unit = line.purchase_price / (1 - line.margin_percent)






