# -*- coding: utf-8 -*-

import logging 
from odoo import models

_logger = logging.getLogger(__name__)

class saleCost(models.Model):
    _inheirt = 'sale.order.line'

    def _prepare_procurement_values(self, group_id=False):
        values = super(saleCost, self)._prepare_procurement_values(group_id)
        
        if self.purchase_price:
            values['custom_sale_cost'] = self.purchase_price
            values['custom_sale_currency_id'] = self.order_id.currency_id.id
            # Log para comprobar qué se está enviando
            _logger.info(f"==== ENVIANDO COSTO DESDE VENTA: {self.purchase_price} ====")
            
        return values 

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _prepare_purchase_order_line(self, product_id, product_qty, product_uom, company_id, values, po):
        res = super(StockRule, self)._prepare_purchase_order_line(
            product_id, product_qty, product_uom, company_id, values, po
        )
        return self._inject_custom_cost(res, values, po)

    def _update_purchase_order_line(self, product_id, product_qty, product_uom, company_id, values, line):
        res = super(StockRule, self)._update_purchase_order_line(
            product_id, product_qty, product_uom, company_id, values, line
        )
        return self._inject_custom_cost(res, values, line.order_id)

    def _inject_custom_cost(self, res, values, po):
        """ Método de apoyo para no repetir código entre crear y actualizar """
        # Log para ver qué viene en la mochila
        _logger.info(f"==== RECIBIENDO VALORES EN COMPRA: {values.get('custom_sale_cost', 'NADA')} ====")
        
        if values.get('custom_sale_cost'):
            sale_cost = values.get('custom_sale_cost')
            sale_currency_id = values.get('custom_sale_currency_id')
            
            sale_currency = self.env['res.currency'].browse(sale_currency_id)
            po_currency = po.currency_id
            
            if sale_currency and sale_currency != po_currency:
                sale_cost = sale_currency._convert(
                    sale_cost, 
                    po_currency, 
                    po.company_id, 
                    po.date_order or fields.Date.today()
                )
            
            # Forzamos el precio unitario
            res['price_unit'] = sale_cost
            
        return res
    