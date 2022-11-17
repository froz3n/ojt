
import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    down_payment = fields.Float(string="Down Payment")
    total = fields.Float(string="Total",compute="get_total")
    vendor_email = fields.Char(related='partner_id.email',store=True,depends=['partner_id'])

    @api.depends('amount_total','down_payment')
    def get_total(self):
        for line in self:
            totals = line.amount_total - line.down_payment
            line.total = totals
        
class PurchaseLineOrder(models.Model):
    _inherit = "purchase.order.line"

    price_diffs = fields.Float(string="Price Difference",compute="get_diffs")
    list_price = fields.Float(string="Cost Price",related="product_id.standard_price")

    @api.depends('list_price','price_unit')
    def get_diffs(self):
        for line in self:
            diffs = line.price_unit - line.list_price
            line.price_diffs = diffs