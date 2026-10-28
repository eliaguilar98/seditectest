from odoo import models, _
from odoo.exceptions import UserError

class CrmLead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    def action_apply(self):
        # 1. Obtener el ID del registro desde el contexto activo
        lead_id = self.env.context.get('active_id')
        
        if lead_id:
            lead = self.env['crm.lead'].browse(lead_id)
            
            # 2. Confirmar que efectivamente es un Lead antes de validar
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
                        'No se puede convertir a Oportunidad.\n'
                        'Faltan datos obligatorios en la Iniciativa:\n- %s'
                    ) % '\n- '.join(missing_fields))

        # 3. Si pasa la validación, continúa con el proceso nativo de conversión
        return super(CrmLead2OpportunityPartner, self).action_apply()