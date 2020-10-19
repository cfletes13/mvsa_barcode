# -*- coding: utf-8 -*-
{
    'name': 'Mvsa Stock Barcode',
    'summary': """Disable Inventoy Adjustment""",
    'version': '12.0.1.0',
    'description': """Disable Inventoy Adjustment""",
    'author': 'Comercialiadora Marvel S.A de C.V',
    'company': 'Comercialiadora Marvel S.A de C.V',
    'website': 'http://www.marvelsa.com',
    'category': 'Stock Barcode',
    'depends': ['barcodes', 'stock', 'web_tour'],
    'license': 'OPL-1',
    'data': [
        #    'views/import.xml',
        #    'views/pos_order.xml',
        'views/stock_barcode_templates.xml',
    ],
    'qweb': ['static/src/xml/mvsa_qweb_templates.xml'],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
