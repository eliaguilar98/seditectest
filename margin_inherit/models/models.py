# -*- coding: utf-8 -*-

from odoo import models, fields, api


class margin_inherit(models.Model):
    _inherit = "sale.order.line"

    margin_percent = fields.Float(
        readonly = False
    )

    price_unit = fields.Float(
        compute = '_compute_price_unit'
    )

    purchase_price = fields.Float()

    margin = fields.Float(
        compute = '_compute_price_unit'
    )

    @api.depends('price_unit','purchase_price','margin_percent','margin','price_subtotal','product_uom_qty')
    def _compute_price_unit(self):
        for line in self:
            line.price_unit = line.purchase_price + (line.purchase_price * line.margin_percent)
            #line.margin = (line.price_unit * line.product_uom_qty) - (line.purchase_price * line.product_uom_qty)
            line.margin = line.margin_percent * line.price_subtotal

    @api.depends()
    def _compute_margin(self):
       for line in self:
            pass






