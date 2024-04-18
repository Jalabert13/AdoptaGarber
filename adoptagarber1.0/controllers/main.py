from odoo import http
from odoo.http import request


class Adopcion(http.Controller):
    
    @http.route('/adopta-results', website=True, auth='public')
    def mostrarAnimales(self, **kw):
        animales = request.env['garber.pets'].sudo().search([])
        print("mascotas---", animales)

        return http.request.render('adoptagarber.mascotas_table', {
            'mascotas': animales,
        })