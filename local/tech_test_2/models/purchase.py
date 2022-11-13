
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
        totals = self.amount_total - self.down_payment
        self.total = totals
        
class PurchaseLineOrder(models.Model):
    _inherit = "purchase.order.line"

    price_diffs = fields.Float(string="Difference w/ Sale Price",compute="get_diffs")
    list_price = fields.Float(related="product_id.lst_price")
    std_price = fields.Float(related="price_unit")

    @api.depends('list_price','std_price')
    def get_diffs(self):
        for line in self:
            if line.list_price and line.std_price :
                diffs = line.list_price - line.std_price
                line.price_diffs = diffs
            else :
                diffs = self.list_price - self.std_price
                self.price_diffs = diffs