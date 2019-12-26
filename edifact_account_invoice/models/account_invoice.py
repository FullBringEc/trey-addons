# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    edi_doc_id = fields.Many2one(
        comodel_name='edifact.document',
        string='Export')
