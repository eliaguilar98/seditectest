# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sales_inherit_lines(models.Model):
     _inherit = "sale.order.line"

     margin_percent = fields.Float(
         readonly=False,
         compute= '_margin'
     )
     price_unit = fields.Float(
         compute = '_compute_price_unit'
     )

     purchase_price = fields.Float()
        
     @api.depends('price_unit','purchase_price','margin_percent')
     def _compute_price_unit(self):
         for line in self:
             line.price_unit = line.purchase_price + (line.purchase_price * line.margin_percent)

     @api.depends('margin_percent')
     def _margin(self):
         for line in self: 
            return line.margin_percent