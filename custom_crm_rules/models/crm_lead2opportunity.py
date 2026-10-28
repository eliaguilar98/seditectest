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
                
                if not lead.email_from:
                    missing_fields.append('Correo Electrónico')
                if not lead.mobile and not lead.phone:
                    missing_fields.append('Teléfono / Móvil')
                if not lead.description:
                    missing_fields.append('Detalle de la Solicitud / Notas')

                if missing_fields:
                    raise UserError(_(
                        'No se puede convertir a Oportunidad.\n'
                        'Faltan datos obligatorios en la Iniciativa:\n- %s'
                    ) % '\n- '.join(missing_fields))

        # 3. Si pasa la validación, continúa con el proceso nativo de conversión
        return super(CrmLead2OpportunityPartner, self).action_apply()