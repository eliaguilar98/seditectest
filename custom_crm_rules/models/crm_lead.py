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

    @api.constrains('stage_id', 'expected_revenue', 'x_studio_fabricante', 'message_ids')
    def _check_qualified_stage_requirements(self):
        # Obtener la referencia de la etapa "Calificado"
        qualified_stage = self.env.ref('crm.stage_lead2', raise_if_not_found=False)

        for lead in self:
            # Validar solo si es una oportunidad y se intenta mover a "Calificado"
            if lead.type == 'opportunity' and qualified_stage and lead.stage_id == qualified_stage:
                missing_requeriments = []

                # 1. Validar pronóstico / Ingreso esperado (Debe ser mayor a 0)
                if not lead.expected_revenue or lead.expected_revenue <= 0: 
                    missing_requirements.append("Prónostico / Ingreso Esperado debe ser mayor a 0")

                # 2. Validar Fabricante (Ajusta 'x_fabricante_id' al nombre exacto de tu campo)
                if hasattr(lead, 'x_studio_fabricante') and not lead.x_studio_fabricante:
                    missing_requirements.append('Fabricante')

                # 3. Validar al menos un registro de seguimiento en el Chatter
                # 'comment' identifica notas internas o correos enviados/recibidos
                tracking_records = lead.message_ids.filtered(lambda m: m.message_type in ['comment', 'email'])
                if not tracking_records:
                    missing_requirements.append('Al menos un registro de seguimiento (Nota o Mensaje en el Chatter)')

                # Lanzar excepción modal si falta algún requerimiento
                if missing_requirements:
                    raise UserError(_(
                        'No es posible mover la Oportunidad a la etapa "%s".\n'
                        'Debes cumplir con los siguientes requisitos:\n- %s'
                    ) % (qualified_stage.name, '\n- '.join(missing_requirements)))
            

    

