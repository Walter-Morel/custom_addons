# -*- coding: utf-8 -*-
# from odoo import http


# class CustomTemplateCss(http.Controller):
#     @http.route('/custom_template_css/custom_template_css/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_template_css/custom_template_css/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_template_css.listing', {
#             'root': '/custom_template_css/custom_template_css',
#             'objects': http.request.env['custom_template_css.custom_template_css'].search([]),
#         })

#     @http.route('/custom_template_css/custom_template_css/objects/<model("custom_template_css.custom_template_css"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_template_css.object', {
#             'object': obj
#         })
