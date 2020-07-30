# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018 PRONEXO (<https://www.pronexo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
<<<<<<< HEAD
from openerp import models, fields, api, _
=======
from odoo import models, fields, api, _
>>>>>>> 11.0

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_ean13_code = fields.Char(
            compute="_get_product_info",
            string="EAN",
            store=True
    )

    @api.one
<<<<<<< HEAD
    @api.depends('product_id','product_id.ean13')
    def _get_product_info(self):
        if self.product_id:
            self.product_ean13_code = self.product_id.ean13
=======
    @api.depends('product_id','product_id.barcode')
    def _get_product_info(self):
        if self.product_id:
            self.product_ean13_code = self.product_id.barcode
>>>>>>> 11.0

