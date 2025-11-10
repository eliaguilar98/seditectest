# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloMoneda(http.Controller):
#     @http.route('/modulo_moneda/modulo_moneda', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_moneda/modulo_moneda/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_moneda.listing', {
#             'root': '/modulo_moneda/modulo_moneda',
#             'objects': http.request.env['modulo_moneda.modulo_moneda'].search([]),
#         })

#     @http.route('/modulo_moneda/modulo_moneda/objects/<model("modulo_moneda.modulo_moneda"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_moneda.object', {
#             'object': obj
#         })

