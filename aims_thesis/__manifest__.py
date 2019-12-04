# -*- coding: utf-8 -*-
{
	'name': 'Thesis',
	'version': '1.0',
	'summary': 'Thesis workflow for TGGS students',
	'category': 'Thesis',
	'author': 'Thanh Quang Vu',
	'maintainer': '',
	'company': 'TGGS',
	'website': 'https://www.thanhvu.com',
	'depends': ['base', 'mail', 'aims_student_academic'],
	'data': [
		'security/ir.model.access.csv',
		# 'views/thesis.xml',
		# 'views/thesisprogress.xml',
		# 'views/thesisdefense.xml',
		'menu/thesis_menu.xml',
		'views/publication.xml',
	],
	'installable': True,
	'application': False,
	'auto_install': False,
}