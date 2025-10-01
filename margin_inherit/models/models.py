# -*- coding: utf-8 -*-

from odoo import models, fields, api


class margin_inherit(models.Model):
    _inherit = "sale.order.line"

    margin_percent = fields.Float(
        readonly = False,
    )

    @api.onchange('margin_percent', 'purchase_price')
    def _onchange_margin_percent(self):
        for line in self:
            "Recalcula el precio unitario cuando cambia el margen o el costo"
            if line.purchase_price and line.margin_percent:
                line.price_unit = line.purchase_price / (1 - line.margin_percent)

    @api.onchange('price_unit','purchase_price')
    def _onchange_price_unit(self):
        "Recalcula el margen cuando cambia el precio unitario"
        for line in self:
            if line.purchase_price and line.price_unit:
                line.margin_percent = (1-(line.purchase_price / line.price_unit))






