# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _name = 'modulo_moneda.modulo_moneda'
    _description = 'modulo_moneda.modulo_moneda'
    _inherit = 'account.move'

    @api.model
    def _aplicar_conversion_moneda(self,record,tipo_cambio): 
        """Método helper para aplicar la conversión de moneda
        """
        try:
            lineas_a_actualizar = record.invoice_line_ids.filtered(
                lambda l: l.price_unit and l.price_unit > 0
            )

            if not lineas_a_actualizar:
                _logger.info("ℹ️ No hay líneas para actualizar en la factura %s", record.name)
                return True

            # Registrar precios originales para auditoría.
            precios_originales = {}
            for linea in lineas_a_actualizar:
                precios_originales[linea.id] = linea.price_unit

            # Aplicar conversión
            for linea in lineas_a_actualizar:
                precio_original = linea.price_unit
                nuevo_precio = precio_original / tipo_cambio
                linea.price_unit = nuevo_precio

                _logger.debug(
                    "Línea %d: $%.2f USD -> $%.2f MXN (TC: %.4f)",
                    linea.id, precio_original, nuevo_precio, tipo_cambio
                )
            # Guardar el tipo de cambio aplicado
            if hasattr(record, 'x_studio_tipo_de_cambio'):
                record.x_studio_tipo_de_cambio = tipo_cambio

            # Recalcular impuestos
            record._recompute_tax_lines()

            # Forzar cálculo de todos los totales
            record._recompute_dynamic_lines(recompute_all_taxes=True)
            
            # Verificar consistencia
            total_lineas = sum(lineas_a_actualizar.mapped('price_subtotal'))
            diferencia = abs(total_lineas - record.amount_untaxed)

            if diferencia > 0.10: #Tolerancia de 10 centavos
                _logger.warning(
                    "Pequeña diferencia en totales: Líneas $%.2f vs Factura $%.2f",
                    total_lineas, record.amount_untaxed
                )
            _logger.info(
                "Conversión existosa para factura %s. %d líneas actualizadas. TC: %.4f",
                record.name, len(lineas_a_actualizar), tipo_cambio)
