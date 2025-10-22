# -*- coding: utf-8 -*-

from odoo import models, fields, api


class margin_inherit(models.Model):
    _inherit = "sale.order.line"

    margin_percent = fields.Float(
        readonly = False,
    )
    price_subtotal = fields.Float(
        readonly = False,
    )

    @api.onchange('margin_percent', 'purchase_price')
    def _onchange_margin_percent(self):
        "Recalcula el precio unitario cuando cambia el margen o el costo"
        if not self: 
            return
        # Solo aplica en la línea actual (self representa la linea activa en el formulario)
        line = self[0]

        #Validaciones básicas para evitar división por cero o valores inválidos
        if line.purchase_price and line.margin_percent < 1:
            try: 
                line.price_unit = line.purchase_price / (1 - line.margin_percent)
            except ZeroDivisionError:
                line.price_unit = line.purchase_price
        else: 
            #Si no hay margen válido, no recalcula
            pass

    @api.onchange('price_unit','purchase_price')
    def _onchange_price_unit(self):
        "Recalcula el margen cuando cambia el precio unitario"
        if not self:
            return
        # Solo aplica en la línea actual (self representa la linea activa en el formulario)
        line = self[0]

        # Validaciones básicas para evitar división por cero o valores inválidos
        if line.purchase_price and line.price_unit < 1:
            try:
                line.margin_percent = (1-(line.purchase_price / line.price_unit))
            except ZeroDivisionError:
                line.margin_percent = 0
        else: 
            pass






