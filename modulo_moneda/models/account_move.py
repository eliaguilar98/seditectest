# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('currency_id')
    def _onchange_currency_id_convert_lines(self):
        for move in self:
        
            if move.state == 'draft': 
        
                # Monedas involucradas
                USD = move.company_id.currency_id.search([('name','=','USD')], limit=1)
                MXN = move.company_id.currency_id.search([('name','=','MXN')], limit=1)
                sale_order = self.env['sale.order'].search([('name', '=', move.invoice_origin)], limit=1)
        
                sales_currency = sale_order.pricelist_id.currency_id
                invoice_currency = move.currency_id
                tipo_cambio = sale_order.x_studio_tipo_de_cambio

                if tipo_cambio <= 0: 
                    raise UserError("El tipo de cambio debe ser mayor a cero")
                else: 
                    date = move.invoice_date or move.date 

                    for line in move.invoice_line_ids: 
                        original_price = line.price_unit

                        # Caso 1: De USD a MXN
                        if sales_currency == USD and invoice_currency == MXN:
                            # Convertir USD -> MXN
                            mxn_price = original_price * tipo_cambio
                            line.price_unit = mxn_price
                
                        # Caso 2: De MXN a USD
                        elif invoice_currency == USD: 
                            usd_price = original_price / tipo_cambio
                            line.price_unit = usd_price