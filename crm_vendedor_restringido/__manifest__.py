# -*- coding: utf-8 -*-
{
    'name': "crm_vendedor_restringido",

    'summary': "Restricción de edición del campo Vendedor en CRM.",

    'description': """
Restricción de edición del campo Vendedor en CRM, solo gerencia tiene permitido la edición. 
    """,

    'author': "SEDITEC",
    'website': "https://www.seditec.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','sales_team'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

