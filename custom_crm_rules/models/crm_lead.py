from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('type', 'email_from', 'phone')
    def _check_lead_qualification_data(self):
        """
        Validación de campos obligatorios antes de permitir la conversación nativa de Lead a Oportunidad
        """
        for lead in self: 
            if lead.type == 'lead':
                missing_fields = []

                #Información de la empresa y contacto 
                if not lead.partner_name:
                    missing_fields.append('Nombre de la Empresa o Contacto')
                if not lead.contact_name:
                    missing_fields.append("Nombre de contacto")

                # Información domiciliaria
                if not lead.street: 
                    missing_fields.append("Calle")
                if not lead.city:
                    missing_fields.append("Ciudad")
                if not lead.state_id:
                    missing_fields.append("Estado")
                if not lead.zip:
                    missing_fields.append("Código postal")
                if not lead.country_id:
                    missing_fields.append("País")

                # Información de contacto 
                if not lead.email_from:
                    missing_fields.append("Correo Electrónico")
                if not lead.phone:
                    missing_fields.append('Teléfono o Móvil')
                if not lead.function:
                    missing_fields.append("Puesto de trabajo")

                # Información contextual de la empresa
                if not lead.description:
                    missing_fields.append('Detalle de la Solicitud / Notas')

                if missing_fields: 
                    raise UserError(_(
                        'No es posible convertir la Iniciativa a Oportunidad.\n'
                        'Debes completar los siguientes campos obligatorios primero:\n- %s'
                    ) % '\n- '.join(missing_fields))

            

    

