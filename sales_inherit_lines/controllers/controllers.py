# -*- coding: utf-8 -*-
# from odoo import http


# class SalesInheritLines(http.Controller):
#     @http.route('/sales_inherit_lines/sales_inherit_lines', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_inherit_lines/sales_inherit_lines/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_inherit_lines.listing', {
#             'root': '/sales_inherit_lines/sales_inherit_lines',
#             'objects': http.request.env['sales_inherit_lines.sales_inherit_lines'].search([]),
#         })

#     @http.route('/sales_inherit_lines/sales_inherit_lines/objects/<model("sales_inherit_lines.sales_inherit_lines"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_inherit_lines.object', {
#             'object': obj
#         })

