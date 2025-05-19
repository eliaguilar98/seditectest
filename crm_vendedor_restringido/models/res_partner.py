# -*- coding: utf-8 -*-

from odoo import models, fields, api 

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'user_id' in vals and not self.env.user.has_group('sales_team.group_sale_manager'):
                raise UserError(_("Solo un gerente de ventas puede asignar un vendedor."))
        return super().create(vals)

    def write(self, vals):
        if 'user_id' in vals:
            for lead in self:
                if not self.env.user.has_group('sales_team.group_sale_manager'):
                    raise ValidationError(_("Solo un gerente de ventas puede cambiar el vendedor asignado."))

        return super().write(vals)