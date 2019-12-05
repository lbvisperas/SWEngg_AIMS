# -*- coding: utf-8 -*-

{
    'name': 'TGGS Grades',
    'version': '12.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Grades',
    'complexity': "easy",
    'author': 'Lianne Visperas',
    'depends': ['base', 'aims_student_academic'],
    'data': [
        'security/ir.model.access.csv',
        'views/assignment_view.xml',
        'views/assignment_sub_line_view.xml',
        'views/student_view.xml',
        'menus/op_menu.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
