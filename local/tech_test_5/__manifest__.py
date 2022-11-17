# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Tech Test 5',
    'category': 'Inventory',
    'author': 'Sonny',
    'version': '1.0',
    'website': 'http://www.solvera.id/',
    'description': """
       hanya untuk latihan
    """,
    'data': [
        'reports/purchase_order_templates.xml',
        'reports/purchase_reports.xml'
    ],
    "depends": [
        "base","purchase","tech_test_2","contacts"
    ],
    'installable': True,
    "images":['static/logo.png'],
}
