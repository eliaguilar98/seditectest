# -*- coding: utf-8 -*-
# from odoo import http


# class CrmVendedorRestringido/(http.Controller):
#     @http.route('/crm_vendedor_restringido//crm_vendedor_restringido/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_vendedor_restringido//crm_vendedor_restringido//objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_vendedor_restringido/.listing', {
#             'root': '/crm_vendedor_restringido//crm_vendedor_restringido/',
#             'objects': http.request.env['crm_vendedor_restringido/.crm_vendedor_restringido/'].search([]),
#         })

#     @http.route('/crm_vendedor_restringido//crm_vendedor_restringido//objects/<model("crm_vendedor_restringido/.crm_vendedor_restringido/"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_vendedor_restringido/.object', {
#             'object': obj
#         })

