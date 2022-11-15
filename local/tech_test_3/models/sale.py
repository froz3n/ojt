
import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta

class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_warehouse = fields.Many2one("stock.warehouse",string="Warehouse")
    sale_warehouse_all = fields.Boolean(string="All Warehouse")