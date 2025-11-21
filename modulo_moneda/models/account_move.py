# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('currency_id')
    def _onchange_currency_id_convert_lines(self):
        for move in self: 
            if move.move_type not in ('out_invoice','in_invoice'):
                continue # Solo aplica a facturas

            if not move.currency_id or not move.company_id: 
                continue

            company = move.company_id
            factura_currency = move.currency_id
            company_currency = company.currency_id

            # Obtener tipo de cambio vigente
            rate = factura_currency._get_conversion_rate(
                company_currency,
                factura_currency,
                company,
                move.invoice_date or fields.Date.context_today(move)
            )

            if not rate: 
                raise UserError("No existe un tipo de cambio válido para la fecha")

            #Convertimos cada linea
            for line in move.invoice_line_ids:
                if line.price_unit:
                    line.price_unit = company_currency.convert(
                        line.price_unit,
                        factura_currency,
                        company,
                        move.invoice_date or fields.Date.context_today(move)
                    )
            # Forzar recálculo de impuestos totales
            move._recompute_dynamic_lines(recompute_all_taxes=True)
            move._onchange_invoice_line_ids()