# -*- coding: utf-8 -*-
{
    'name': "crm_vendedor_restringido",

    'summary': "Restringe la edición del campo Vendedor Asignado en oportunidades del CRM.",

    'description': """
Este módulo agrega restricciones para evitar cambios no autorizados en el campo "Vendedor Asignado" dentro de las oportunidades del CRM.

Ideal para asegurar la trazabilidad comercial y evitar reasignaciones no controladas por parte de los usuarios. 
    """,

    'author': "SEDITEC",
    'website': "https://www.seditec.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '19.0.1.1',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','sales_team'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'views/res_partner_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}

