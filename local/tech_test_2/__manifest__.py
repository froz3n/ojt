# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Tech Test 2',
    'category': 'Inventory',
    'author': 'Sonny',
    'version': '1.0',
    'website': 'http://www.solvera.id/',
    'description': """
       hanya untuk latihan
    """,
    'data': [
        'views/purchase_order_view.xml',
    ],
    "depends": [
        "purchase"
    ],
    'installable': True,
    "images":['static/logo.png'],
}
