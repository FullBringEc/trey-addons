# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.
from openerp import models, fields


class CollaborationReason(models.Model):
    _name = 'collaboration.reason'

    name = fields.Char(
        string='Name')
