# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # 1. Campo margen simple y almacenable
    margin_percent = fields.Float(
        string="Margen (%)",
        store=True,
        readonly=False,
    )

    # 2. Respetamos el campo costo, pero forzamos a Odoo a no sobreescribirlo 
    # si el usuario ya interactuó con el margen
    purchase_price = fields.Float(
        store=True, 
        readonly=False,
        precompute=True
    )

    # 3. INTERCEPTAMOS EL COSTO NATIVO (Esto evita que al confirmar vuelva a 216.102)
    @api.depends('product_id', 'company_id', 'currency_id', 'product_uom')
    def _compute_purchase_price(self):
        # 3.1. Dejamos que Odoo traiga el costo original primero
        super()._compute_purchase_price()
        
        # 3.2. Si el usuario ya estableció un margen, obligamos a Odoo a respetar el costo manual (220)
        for line in self:
            if line.margin_percent > 0.0 and line.price_unit:
                line.purchase_price = line.price_unit * (1.0 - line.margin_percent)

    # 4. USAMOS ONCHANGE PARA LA PANTALLA (Esto evita que el Amount quede en 0.06)
    @api.onchange('margin_percent', 'purchase_price')
    def _onchange_margin_percent_ui(self):
        for line in self:
            if line.purchase_price and 0.0 < line.margin_percent < 1.0:
                line.price_unit = line.purchase_price / (1.0 - line.margin_percent)

    @api.onchange('price_unit', 'purchase_price')
    def _onchange_price_unit_ui(self):
        for line in self:
            if line.purchase_price and line.price_unit:
                line.margin_percent = 1.0 - (line.purchase_price / line.price_unit)
            elif not line.price_unit:
                line.margin_percent = 0.0




