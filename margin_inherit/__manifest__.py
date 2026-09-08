# -*- coding: utf-8 -*-
{
    'name': "margin_inherit",

    'summary': "Permite la modificación del campo Margen % y calcula automáticamente el precio unitario en las líneas de venta. ",

    'description': """
Este módulo extiende la funcionalidad de ventas para: 
- Permitir la modificación del campo Margen % en las líneas de pedido. 
- Calcular automáticamente el precio unitario tomando en cuenta el costo del producto y el margen definido. 

Ideal para equipos que trabajan con estrategias de precio basadas en márgenes comerciales.  
    """,

    'author': "SEDITEC",
    'website': "https://www.seditec.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '18.0.1.1',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management','sale_margin'],

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

