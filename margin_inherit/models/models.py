# -*- coding: utf-8 -*-

from odoo import models, fields, api


class margin_inherit(models.Model):
    _inherit = "sale.order.line"

    margin_percent = fields.Float(
        sting = "Margen (%)",
        readonly = False,
    )
    #price_subtotal = fields.Float(
     #   readonly = False,
    #)

    @api.onchange('margin_percent', 'purchase_price')
    def _onchange_margin_percent(self):
        "Recalcula el precio unitario cuando cambia el margen o el costo"
        for line in self:
            # Asegura que el costo exista y el margen sea menor al 100%
            # (Un margen de 1.0 causaría división por cero
            if line.purchase_price and line.margin_percent < 1.0: 
                line.price_unit = line.purchase_price / (1 - line.margin_percent)

    @api.onchange('price_unit','purchase_price')
    def _onchange_price_unit(self):
        "Recalcula el margen cuando cambia el precio unitario"
        for line in self:
            # Previene ZeroDivisionError verificando que price_unit no sea 0
            if line.purchase_price and line.price_unit:
                line.margin_percent = 1.0 - (line.purchase_price / line.price_unit)
            elif not line.price_unit:
                line.margin_percent = 0.0






