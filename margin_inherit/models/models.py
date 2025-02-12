# -*- coding: utf-8 -*-

from odoo import models, fields, api


class margin_inherit(models.Model):
    _inherit = "sale.order"

    margin_percent = fields.Float(
        readonly = False,
        compute = '_compute_margin'
    )

    price_unit = fields.Float(
        compute = '_compute_price_unit'
    )

    purchase_price = fields.Float()

    @api.depends('order_line.price_unit','order_line.purchase_price','order_line.margin_percent')
    def _compute_price_unit(self):
        for line in self:
            line.price_unit = line.purchase_price + (line.purchase_price * line.margin_percent)

    @api.depends('order_line.margin', 'amount_untaxed')
    def _compute_margin(self):
        pass






