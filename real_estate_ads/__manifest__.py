# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Real Estate Ads',
    'version': '1.1',
    'category': 'Marketing',
    'sequence': 30,
    'summary': 'Manage planning , budgeting and forecasting',
    'description': """
Real Estate Ads
========================
Selling and buying of real estate properties
""",
    'website': 'https://www.odoo.com/',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/room.xml",
        "views/real_estate_ads.xml",
        "views/menu_items.xml"
    ],
    'demo': [''],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
    'assets': {
    }
}
