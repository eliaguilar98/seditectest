# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime 

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
                    raise ValidationError(_("🔒 Solo un gerente de ventas tiene permiso para cambiar el vendedor asignado.Si necesitas hacer este cambio, por favor contacta a tu gerente."))

                # Obtener datos del vendedor anterior y nuevo 
                old_user = lead.user_id
                new_user = self.env['res.users'].browse(vals['user_id'])

                if old_user != new_user: 
                    timestamp = fields.Datetime.context_timestamp(self.with_context(tz=self.env.user.tz),datetime.now())
                    formatted_time = fields.Datetime.to_string(timestamp)
                    lead.message_post(
                        body =_(
                            "📝 Asignación de vendedor modificada\n"
                            "- Anterior: %s\n"
                            "- Nuevo: %s\n"
                            "- Modificado por: %s\n"
                            "- Fecha y hora: %s"
                        ) % (
                            old_user.name or _("Sin asignar"),
                            new_user.name or _("Sin asignar"),
                            self.env.user.name,
                            formatted_time
                        ),
                        subtype_xmlid="mail.mt_note",
                    )

        return super().write(vals)# Obtener datos del vendedor anterior y nuevo 
                old_user = lead.user_id
                new_user = self.env['res.users'].browse(vals['user_id'])

                if old_user != new_user: 
                    lead.message_post(
                        body =_("El vendedor asignado fu cambiado de <b>%s</b> a <b>%s</b> por <i>%s</i>.") % (
                            old_user.name or _("Sin asignar"),
                            new_user.name or _("Sin asignar"),
                            self.env.user.name,
                        ),
                        subtype_xmlid="mail.mt_note",
                    )
        return super().write(vals)