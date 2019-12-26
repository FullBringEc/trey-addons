# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2017-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Sale Line Comment',
    'summary': 'Sale Line Comment',
    'description': '''
This module allows to add comments in sale and invoice lines. If quantity and
price unit are zero, lines will display as comments in reports, with hidden
quantity, price unit, discount, taxes and subtotal. ''',
    'author': 'Trey (www.trey.es)',
    'website': 'https://www.trey.es',
    'category': 'Sales',
    'version': '8.0.1.0.0',
    'depends': [
        'sale',
        'sale_layout',
        'account',
    ],
    'data': [
        'reports/account_invoice_report.xml',
        'reports/sale_order_report.xml',
    ],
    'installable': True,
}
