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
                sale_order = env['sale.order'].search([('name', '=', record.invoice_origin)], limit=1)
        
                sales_currency = sale_order.pricelist_id.currency_id
                invoice_currency = move.currency_id
        
                if sales_currency == USD and invoice_currency == MXN:
                    date = move.invoice_date or move.date
            
                    for line in move.invoice_line_ids:
                    # Convertir USD -> MXN
                        converted = USD._converted(
                            line.price_unit,
                            MXN,
                            move.company_id,
                            date)
                    
                        line.price_unit = converted