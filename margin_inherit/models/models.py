# -*- coding: utf-8 -*-
from odoo import models, fields, api

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # 1. Hacemos que los campos NATIVOS sean completamente editables
    margin_percent = fields.Float(readonly=False, store=True)
    purchase_price = fields.Float(readonly=False, store=True)

    # 2. PROTEGEMOS EL COSTO (purchase_price) PARA QUE NO VUELVA A 216.102 AL CONFIRMAR
    def _compute_purchase_price(self):
        # Respaldamos el costo manual actual que el vendedor puso en pantalla
        manual_costs = {}
        for line in self:
            if line.purchase_price > 0:
                manual_costs[line] = line.purchase_price

        # Dejamos que Odoo ejecute su cálculo normal (que traerá el 216.102)
        super()._compute_purchase_price()

        # Le devolvemos el valor que el vendedor escribió (220)
        # Solo aplicamos esto si el vendedor efectivamente definió un margen manual
        for line in self:
            if line in manual_costs and line.margin_percent > 0.0:
                line.purchase_price = manual_costs[line]

    # 3. PROTEGEMOS EL PRECIO DE VENTA (price_unit)
    def _compute_price_unit(self):
        manual_prices = {}
        for line in self:
            if line.price_unit > 0 and line.margin_percent > 0.0:
                manual_prices[line] = line.price_unit

        super()._compute_price_unit()

        for line in self:
            if line in manual_prices:
                line.price_unit = manual_prices[line]

    # 4. TUS ONCHANGES (Idénticos a tu lógica, controlan lo que se ve en la pantalla)
    @api.onchange('margin_percent', 'purchase_price')
    def _onchange_margin_percent(self):
        """Recalcula el precio unitario cuando cambia el margen o el costo"""
        for line in self:
            if line.purchase_price and 0.0 < line.margin_percent < 1.0:
                line.price_unit = line.purchase_price / (1.0 - line.margin_percent)

    @api.onchange('price_unit', 'purchase_price')
    def _onchange_price_unit(self):
        """Recalcula el margen cuando cambia el precio unitario"""
        for line in self:
            if line.purchase_price and line.price_unit:
                line.margin_percent = 1.0 - (line.purchase_price / line.price_unit)
            elif not line.price_unit:
                line.margin_percent = 0.0

    # 5. RESETEO AL CAMBIAR DE PRODUCTO
    @api.onchange('product_id')
    def _onchange_product_id_reset_margin(self):
        """Si el vendedor quita el producto y pone otro, reseteamos el margen 
        a 0 para permitir que Odoo traiga los costos estándar del nuevo producto."""
        for line in self:
            line.margin_percent = 0.0