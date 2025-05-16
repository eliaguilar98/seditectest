# -*- coding: utf-8 -*-

from odoo import models, fields, api 

class crm_Lead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        if 'user_id' in vals and not self.env.user.has_group('sales_team.group_sale_manager'):
            raise UserError(_("Solo un gerente de ventas puede asignar un vendedor."))
        return super().create(vals)

    def write(self, vals):
        if 'user_id' in vals and not self.env.user.has_group('sales_team.group_sale_manager'):
            raise ValidationError(_("Solo un gerente de ventas puede cambiar el vendedor asignado."))

        return super().write(vals)
