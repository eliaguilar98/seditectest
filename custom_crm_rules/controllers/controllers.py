# from odoo import http


# class CustomCrmRules/(http.Controller):
#     @http.route('/custom_crm_rules//custom_crm_rules/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_crm_rules//custom_crm_rules//objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_crm_rules/.listing', {
#             'root': '/custom_crm_rules//custom_crm_rules/',
#             'objects': http.request.env['custom_crm_rules/.custom_crm_rules/'].search([]),
#         })

#     @http.route('/custom_crm_rules//custom_crm_rules//objects/<model("custom_crm_rules/.custom_crm_rules/"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_crm_rules/.object', {
#             'object': obj
#         })

