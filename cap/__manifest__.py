# -*- coding: utf-8 -*-
{
    'name': "cap",

    'summary': """
        este es un modulo de prueba wilson vargas""",

    'description': """
        modulo CAP
    """,

    'author': "wilson vargas",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CAPACITACION',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    # only loaded in demonstration mode
    #'demo': [
        #'demo/demo.xml',
    ], 
    "installable": True,
}
