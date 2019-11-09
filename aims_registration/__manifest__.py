# -*- coding: utf-8 -*-
{
    'name': "Course Registration",

    'summary': """
        Register for courses""",

    'description': """
        This module will allow students to register for the course
    """,

    'author': "Mandeep Khadka",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'AIMS',
    'version': '12.0.0.0',

    # any module necessary for this one to work correctly
    # ISSUE: Cannot connect this in the menu <=> basing on openeducat
    'depends': ['base', 'aims_student_academic'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/registration_view.xml',
        'menus/registration_menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
    'sequence': 1,
}