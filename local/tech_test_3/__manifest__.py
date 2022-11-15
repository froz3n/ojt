# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Tech Test 3',
    'category': 'Inventory',
    'author': 'Sonny',
    'version': '1.0',
    'website': 'http://www.solvera.id/',
    'description': """
       hanya untuk latihan
    """,
    'data': [
        'views/sale_order_views.xml',
    ],
    "depends": [
        "sale","stock"
    ],
    'installable': True,
    "images":['static/logo.png'],
}
