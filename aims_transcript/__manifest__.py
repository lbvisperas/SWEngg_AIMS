# -*- coding: utf-8 -*-
{
    'name': 'Transcript',
    'version': '1.0',
    'summary': 'Record of Student Transcript Information',
    'category': 'Education and Employment',
    'author': 'Tran Lan Anh',
    'maintainer': 'Tran Lan Anh',
    'company': 'Lan',
    'website': 'https://www.tggs.kmutnb.ac.th',
    'depends': ['base', 'aims_student_academic'],
    'data': [
        'security/transcript_security.xml',
        'reports/report_menu.xml',
        'security/ir.model.access.csv',
        'reports/report_transcript.xml',
        'views/transcript_view.xml',
        'views/grades_view.xml',
        'views/student_grades_view.xml',
        'menu/transcript_menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

