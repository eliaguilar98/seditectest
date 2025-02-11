# -*- coding: utf-8 -*-
# from odoo import http


# class MarginInherit(http.Controller):
#     @http.route('/margin_inherit/margin_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/margin_inherit/margin_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('margin_inherit.listing', {
#             'root': '/margin_inherit/margin_inherit',
#             'objects': http.request.env['margin_inherit.margin_inherit'].search([]),
#         })

#     @http.route('/margin_inherit/margin_inherit/objects/<model("margin_inherit.margin_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('margin_inherit.object', {
#             'object': obj
#         })

