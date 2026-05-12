# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateCost(http.Controller):
#     @http.route('/update_cost/update_cost', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_cost/update_cost/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_cost.listing', {
#             'root': '/update_cost/update_cost',
#             'objects': http.request.env['update_cost.update_cost'].search([]),
#         })

#     @http.route('/update_cost/update_cost/objects/<model("update_cost.update_cost"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_cost.object', {
#             'object': obj
#         })

