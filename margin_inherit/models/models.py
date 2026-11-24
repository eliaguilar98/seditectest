# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # 1. Hacemos editables los campos sin romper el flujo de cómputo
    margin_percent = fields.Float(readonly=False, store=True)
    purchase_price = fields.Float(readonly=False, store=True)

    # 2. PROTEGEMOS EL COSTO (purchase_price)
    def _compute_purchase_price(self):
        # Si la línea ya existe en BD o el usuario lo dejó explícitamente en 0 tras editar,
        # solo recalculamos automáticamente cuando cambia el producto o la UdM
        manual_costs = {}
        for line in self:
            # Guardamos el costo actual si no es una línea recién creada sin costo
            if line._origin and line.product_id == line._origin.product_id and line.product_uom_id == line._origin.product_uom_id:
                manual_costs[line] = line.purchase_price

        super()._compute_purchase_price()

        for line in self:
            if line in manual_costs:
                line.purchase_price = manual_costs[line]

    # 3. PROTEGEMOS EL PRECIO DE VENTA (price_unit)
    def _compute_price_unit(self):
        manual_prices = {}
        for line in self:
            if line._origin and line.product_id == line._origin.product_id and line.product_uom_id == line._origin.product_uom_id:
                manual_prices[line] = line.price_unit

        super()._compute_price_unit()

        for line in self:
            if line in manual_prices:
                line.price_unit = manual_prices[line]

    # 4. SOBRESCRIBIMOS _compute_margin PARA EVITAR RESIDUOS EN CACHÉ
    @api.depends('price_subtotal', 'product_uom_qty', 'purchase_price')
    def _compute_margin(self):
        super()._compute_margin()
        for line in self:
            # Si precio y costo son 0, forzamos margen en 0 limpio
            if not line.price_subtotal and not line.purchase_price:
                line.margin = 0.0
                line.margin_percent = 0.0

    # 5. ONCHANGES EN PANTALLA
    @api.onchange('margin_percent')
    def _onchange_margin_percent(self):
        """Recalcula el precio unitario solo cuando el usuario edita el margen %"""
        for line in self:
            if line.purchase_price and 0.0 < line.margin_percent < 1.0:
                line.price_unit = line.purchase_price / (1.0 - line.margin_percent)

    @api.onchange('price_unit', 'purchase_price')
    def _onchange_price_unit_or_cost(self):
        """Recalcula el margen % y el margen monetario en vivo cuando cambia precio o costo"""
        for line in self:
            if line.purchase_price and line.price_unit:
                line.margin_percent = 1.0 - (line.purchase_price / line.price_unit)
            elif not line.price_unit:
                line.margin_percent = 0.0
            # Forzamos actualización visual inmediata del margen monetario
            line.margin = line.price_subtotal - (line.purchase_price * line.product_uom_qty)

    # 6. RESETEO AL CAMBIAR DE PRODUCTO
    @api.onchange('product_id')
    def _onchange_product_id_reset_margin(self):
        for line in self:
            line.margin_percent = 0.0