# -*- coding: utf-8 -*-
{
    'name': "Conversión de Moneda Personalizada",

    'summary': "Aplica tipo de cambio personalizado al facturar",

    'description': """
Este módulo aplica el tipo de cambio personalizado de la orden de venta al generar facturas en pesos mexicano. 
    """,

    'author': "SEDITEC",
    'website': "https://www.seitec.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0.1.1',
    'installable':True,

    # any module necessary for this one to work correctly
    'depends': ['sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}

