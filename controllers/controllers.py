# -*- coding: utf-8 -*-
# from odoo import http


# class RhPlus(http.Controller):
#     @http.route('/rh_plus/rh_plus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rh_plus/rh_plus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rh_plus.listing', {
#             'root': '/rh_plus/rh_plus',
#             'objects': http.request.env['rh_plus.rh_plus'].search([]),
#         })

#     @http.route('/rh_plus/rh_plus/objects/<model("rh_plus.rh_plus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rh_plus.object', {
#             'object': obj
#         })
