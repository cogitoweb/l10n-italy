# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    tax_stamp_product_id = fields.Many2one(
        'product.product', 'Tax Stamp Product',
        help="Product used as Tax Stamp in customer invoices."
        )

    move_line_tax_stamp = fields.Boolean(
        string="Move Line Tax Stamp",
        default=False,
        help="Check this for include tax stamp in move line"
    )


class AccountConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    tax_stamp_product_id = fields.Many2one(
        related='company_id.tax_stamp_product_id',
        readonly=False
        )
