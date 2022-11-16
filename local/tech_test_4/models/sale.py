
import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta

class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_pr_consumable = fields.Float(string='Consumable',compute='get_total_per_type')
    sale_pr_service = fields.Float(string='Service',compute='get_total_per_type')
    sale_pr_stockable = fields.Float(string='Stockable Product',compute='get_total_per_type')

    sale_pr_consumable_exist = fields.Boolean(compute='get_total_per_type')
    sale_pr_service_exist = fields.Boolean(compute='get_total_per_type')
    sale_pr_stockable_exist = fields.Boolean(compute='get_total_per_type')
        
    @api.onchange('order_line')
    def get_total_per_type(self):
        for order in self:
            self.sale_pr_consumable = self.sale_pr_service = self.sale_pr_stockable = 0.0
            self.sale_pr_consumable_exist = self.sale_pr_service_exist = self.sale_pr_stockable_exist = False
            for line in order.order_line:
                if line.product_id.type == 'consu':
                    self.sale_pr_consumable += line.price_subtotal
                    self.sale_pr_consumable_exist = True
                elif line.product_id.type == 'service':
                    self.sale_pr_service += line.price_subtotal
                    self.sale_pr_service_exist = True
                elif line.product_id.type == 'product':
                    self.sale_pr_stockable += line.price_subtotal
                    self.sale_pr_stockable_exist = True