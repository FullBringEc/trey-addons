# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import fields, models, api


class EdifactAccountVoucherImport(models.TransientModel):
    _name = 'edifact.account.voucher.import'
    _description = 'Import account voucher from edi'

    @api.model
    def _get_files_to_import(self):
        files = self.env['edifact.document'].read_in_files('vouchers')
        return '\n'.join([f for f in files])

    files_to_import = fields.Text(
        string='Files to import',
        default=_get_files_to_import)

    @api.multi
    def action_import(self):
        edi_doc = self.env['edifact.document'].process_voucher_in_files()
        if not edi_doc:
            return
        value = {
            'view_type': 'form',
            'view_mode': 'form,tree',
            'res_model': 'edifact.document',
            'res_id': edi_doc.id,
            'type': 'ir.actions.act_window',
            'nodestroy': True
        }
        return value
