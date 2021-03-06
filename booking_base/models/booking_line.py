# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class BookingLine(models.Model):
    _name = 'booking.line'
    _description = 'Booking Line'
    _order = 'date desc, name desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    booking_id = fields.Many2one(
        comodel_name='booking',
        string='Booking',
        required=True,
        ondelete='cascade',
        select=True)
    line_agency_id = fields.Many2one(
        comodel_name='res.partner',
        related='booking_id.agency_id',
        store=True)
    name = fields.Char(
        size=250,
        string='Service',
        help='Service Name for Booking line')
    booking_code = fields.Char(
        related='booking_id.name',
        select=True,
        store=True)
    date = fields.Datetime(
        string='Date',
        required=True,
        select=True)
    canceled = fields.Boolean(
        string='Canceled')
    markup = fields.Integer(
        string='Markup')
    ex_reference = fields.Char(
        string='External Ref.')
    selling_price = fields.Float(
        string='Selling Price',
        track_visibility='onchange')
    cost_currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Cost Currency')
    sell_currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Seller Currency')
    cost_net = fields.Float(
        string='Net Cost',
        track_visibility='onchange')
    base_change_factor = fields.Float(
        string='Base Change Factor')
    cost_change_factor = fields.Float(
        string='Cost Change Factor')
    pricecommission = fields.Float(
        string='Price Commission',
        track_visibility='onchange')
    commission = fields.Float(
        string='Commission',
        track_visibility='onchange')
    per_commission = fields.Float(
        string='Commission %')
    amount_untaxed = fields.Float(
        string='Amount Untaxed')
    amount = fields.Float(
        string='Amount',
        track_visibility='onchange')
    amount_cancel = fields.Float(
        string='Amount Cancelation',
        track_visibility='onchange')
    date_init = fields.Datetime(
        string='Begin Travel')
    date_end = fields.Datetime(
        string='End Travel')
    supplier_id = fields.Many2one(
        comodel_name='res.partner',
        string='Supplier')
    zone_id = fields.Many2one(
        comodel_name='booking.zone',
        string='Zone')
    zone_name = fields.Char(
        string='Zone',
        store=True,
        related='zone_id.name')
    zone_province = fields.Char(
        string='Province',
        store=True,
        related='zone_id.province')
    zone_country = fields.Char(
        string='Country',
        store=True,
        related='zone_id.country')
    invoiced = fields.Boolean(
        string='Invoiced',
        track_visibility='onchange')
    supplier_invoice_number = fields.Char(
        string='Supplier Invoice Number')
