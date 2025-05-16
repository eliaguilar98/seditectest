# -*- coding: utf-8 -*-

from odoo import models, fields, api 

class crm_Lead(models.Model):
    _inherit = 'crm.lead'

    can_edit_user_id = fields.Boolean(compute='_compute_can_edit_user_id', store=False)

    @api.depends()
    def _compute_can_edit_user_id(self):
        for record in self:
            user = self.env.user
            record.can_edit_user_id = user.has_group('sales_team.group_sale_manager')
