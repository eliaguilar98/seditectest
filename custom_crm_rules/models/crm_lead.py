from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('type', 'email_from', 'phone', 'mobile')
    def _check_lead_qualification_data(self):
        """
        Validación de campos obligatorios antes de permitir la conversación nativa de Lead a Oportunidad
        """
        for lead in self: 
            if lead.type == 'lead':
                missing_fields = []

                if not lead.email_from:
                    missing_fields.append("Correo Electrónico")
                if not lead.mobile and not lead.phone:
                    missing_fields.append('Teléfono o Móvil')
                if not lead.partner_name and not lead.contact_name:
                    missing_fields.append('Nombre de la Empresa o Contacto')
                if not lead.description:
                    missing_fields.append('Detalle de la Solicitud / Notas')

                if missing_fields: 
                    raise UserError(_(
                        'No es posible convertir la Iniciativa a Oportunidad.\n'
                        'Debes completar los siguientes campos obligatorios primero:\n- %s'
                    ) % '\n- '.join(missing_fields))

            

    

