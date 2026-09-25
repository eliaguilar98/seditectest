# -*- coding: utf-8 -*-

from odoo import models, fields, api


class margin_inherit(models.Model):
    _inherit = "sale.order.line"

    # 1. Definimos el margen como un campo computado pero editable (readonly=False)
    margin_percent = fields.Float(
        string="Margen (%)",
        compute='_compute_margin_percent',
        inverse='_inverse_margin_percent',
        store=True,
        readonly=False,
        precompute=True # Fundamental en Odoo 17+ para calcular antes de guardar
    )

    # 2. El método compute calcula el margen si cambia el precio o el costo 
    @api.depends('price_unit', 'purchase_price')
    def _compute_margin_percent(self):
        "Recalcula el precio unitario cuando cambia el margen o el costo"
        for line in self:
            if line.price_unit and line.purchase_price: 
                line.margin_percent = 1.0 - (line.purchase_price / line.price_unit)
            else:
                # Evita sobreescribir 0.0 si el usuario está tipeando un nuevo registro
                if not line.margin_percent: 
                    line.margin_percent = 0.0

 # 3. El método inverse calcula el precio unitario si el usuario modifica el margen manual
    def _inverse_margin_percent(self):
        for line in self:
            if line.purchase_price and line.margin_percent < 1.0:
                # Recalcula y asigna el precio unitario de venta
                new_price = line.purchase_price / (1.0 - line.margin_percent)
                if line.price_unit != new_price:
                    line.price_unit = new_price

    # Si quieres que el usuario edite el costo (220) y Odoo NO lo regrese a 216.102
    purchase_price = fields.Float(
        store=True, 
        readonly=False, 
        precompute=True
    )





