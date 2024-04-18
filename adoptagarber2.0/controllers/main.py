from odoo import http
from odoo.http import request


class Adopcion(http.Controller):
    
    @http.route('/adopta-results', website=True, auth='public')
    def mostrarAnimales(self, **kw):
        # Obtener el usuario actual
        user = request.env.user
        
        # Buscar las mascotas asociadas con el usuario actual
        animales = request.env['garber.pets'].sudo().search([('asociacion', '=', user.id)])
        
        print("mascotas---", animales)

        return http.request.render('adoptagarber.mascotas_table', {
            'mascotas': animales,
        })
