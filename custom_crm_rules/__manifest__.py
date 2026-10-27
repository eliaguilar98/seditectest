{
    'name': "CRM Validation Rules & Stage Locks",

    'summary': "Validaciones avanzadas para transiciones de etapas en CRM",

    'description': """
Validaciones avanzadas para transiciones de etapas en CRM
    """,

    'author': "sedITec",
    'website': "https://www.seditec.mx",
    'category': 'Uncategorized',
    'version': '19.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'data/crm_cron.xml',
        'views/crm_lead_views.xml',
      
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

