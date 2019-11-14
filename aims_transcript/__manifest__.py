# -*- coding: utf-8 -*-
{
    'name': "Transcript",

    'summary': "Record of Student Transcript Information",
    'category': "Education and Employment",
    'version': "1.0",
    'author': "Tran Lan Anh",
    'maintainer': "Tran Lan Anh",
    'company': "Lan",
    'website': "https://www.tggs.kmutnb.ac.th",

    'depends': ['base', 'aims_student_academic'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/transcript_view.xml',
        'menu/transcript_menu.xml',
        'reports/report_menu.xml',
        'reports/report_transcript.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
