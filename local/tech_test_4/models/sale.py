
import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta

class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_pr_consumable = fields.Float(string='Consumable',compute='get_total_per_type')
    sale_pr_service = fields.Float(string='Service',compute='get_total_per_type')
    sale_pr_stockable = fields.Float(string='Stockable Product',compute='get_total_per_type')

    sale_pr_consumable_exist = fields.Boolean(default=False)
    sale_pr_service_exist = fields.Boolean(default=False)
    sale_pr_stockable_exist = fields.Boolean(default=False)

    @api.depends('order_line.price_subtotal')
    def get_total_per_type(self):
        for order in self:
            sale_pr_consumable = sale_pr_service = sale_pr_stockable = 0.0
            for line in order.order_line:
                if line.product_id.type == 'consu':
                    sale_pr_consumable += line.price_subtotal
                if line.product_id.type == 'service':
                    sale_pr_service += line.price_subtotal
                if line.product_id.type == 'product':
                    sale_pr_stockable += line.price_subtotal
            order.update({
                'sale_pr_consumable' : sale_pr_consumable,
                'sale_pr_service' : sale_pr_service,
                'sale_pr_stockable' : sale_pr_stockable,
            })
                
    # @api.@api.onchange('')
    # def _onchange_(self):
    #     pass
