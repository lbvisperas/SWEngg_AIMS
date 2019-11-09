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
	# 'depends': ['base','aims_student_academic'],
	'data': [
        # 'security/op_security.xml',
		'security/ir.model.access.csv',
		'menu/transcript_menu.xml',
		'views/transcript.xml',
		'views/grades.xml',
		'views/student.xml'
	],
	'installable': True,
	'application': False,
	'auto_install': False,
}