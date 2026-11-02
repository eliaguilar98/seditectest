from odoo import models, fields, api, _

# 1. Crear el modelo para el catálogo de Puestos
class PartnerJobPosition(models.Model):
    _name = 'res.partner.job.position'
    _description = 'Catálogo de Puestos de Trabajo'

    name = fields.Char(string="Puesto de trabajo", required=True)
    active = fields.Boolean(default=True)

# 2. Extender el modelo de Contactos (res.partner)
class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Campo tipo Many2one hacia el catálogo estandarizado
    job_position_id = fields.Many2one(
        'res.partner.job.position',
        string="Puesto de trabajo",
        help="Seleccione el puesto de trabajo del contacto". 
    )

    
    