# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('currency_id')
    def _onchange_currency_id_convert_lines(self):
        for move in self:
            #if move.move_type not in ('out_invoice', 'in_invoice'): 
            if move.state != 'draft': 
                return

            company_currency = move.company_id.currency_id
            invoice_currency = move.currency_id
            date = move.invoice_date or move.date or fields.Date.today()

            # Obtener tasa de conversión real de Odoo
            rate = invoice_currency._get_conversion_rate(
                from_currency=company_currency,
                to_currency=invoice_currency
            )

            move.message_post(body=f"Tasa aplicada: {rate}")

            # Convertir cada línea
            for line in move.invoice_line_ids:
                if not line.price_unit:
                    continue

                original_price = line.price_unit

                # Convertir desde moneda de la compañía -> nueva moneda
                converted_price = company_currency._convert(
                    original_price, 
                    invoice_currency,
                    move.company_id, 
                    date
                )
                line.price_unit = converted_price

        #for move in self: 
         #   if move.move_type not in ('out_invoice','in_invoice'):
          #      continue # Solo aplica a facturas

           # if not move.currency_id or not move.company_id: 
            #    continue

           # company = move.company_id
            #factura_currency = move.currency_id
            #company_currency = company.currency_id

            ## Obtener tipo de cambio vigente
            #rate = factura_currency._get_conversion_rate(
             #   company_currency,
              #  factura_currency,
               # company,
               # move.invoice_date or fields.Date.context_today(move)
            #)

            #if not rate: 
             #   raise UserError("No existe un tipo de cambio válido para la fecha")

            #Convertimos cada linea
            #for line in move.invoice_line_ids:
             #   if line.price_unit:
              #      line.price_unit = company_currency._convert(
               #         line.price_unit,
                #        factura_currency,
                 #       company,
                  #      move.invoice_date or fields.Date.context_today(move)
                   # )
           