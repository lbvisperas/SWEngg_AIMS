# -*- coding: utf-8 -*-
{
    'name': "Internship",

    'summary': """
        Internship form for students""",

    'description': """
        Internship form for students to get approve from the academic teachers to be able to create weekly report
    """,

    'author': "Nan Than Than Soe",
    'website': "http://www.nanthanthansoe.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education and Internship',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/internship.xml',
        # 'views/report.xml',
        'menu/menu.xml',
    ],
    'installable':True,
    'application':False,
    'auto_install':False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}