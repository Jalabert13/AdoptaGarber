from requests import post
from odoo import http
from odoo.http import request


class Adopcion(http.Controller):

    
    @http.route('/adoptions', website=True, auth='public')
    def mostrarAnimalesFiltrados(self, **kw):

        clase = request.params.get('clase')
        raza = request.params.get('raza')
        edad_min = request.params.get('edad_min')
        edad_max = request.params.get('edad_max')
        esterilizado = bool(request.params.get('esterilizado'))

        # Realizar la búsqueda en la base de datos según los filtros
        animales = request.env['garber.pets'].sudo().search([
            ('clase', '=', clase),
            ('raza', 'ilike', raza),
            ('edad', '>=', edad_min),
            ('edad', '<=', edad_max),
        ])

        # Renderizar la vista con los resultados
        return http.request.render('adoptagarber.filtro_busqueda_animales', {
            'animales': animales,
        })
    
    # @http.route('/adopta-results', website=True, auth='public')
    # def mostrarAnimales(self, **kw):
    #     # Obtener el usuario actual
    #     user = request.env.user
        
    #     # Buscar las mascotas asociadas con el usuario actual
    #     animales = request.env['garber.pets'].sudo().search([('asociacion', '=', user.id)])

    #     return http.request.render('adoptagarber.mascotas_table', {
    #         'mascotas': animales,
    #     })


    @http.route('/adopta-results', website=True, auth='public')
    def mostrarAnimales(self, **kw):
        # Obtener el usuario actual
        user = request.env.user

        # Buscar todas las mascotas si no hay un usuario autenticado
        if not user or user.id == request.website.user_id.id:
            animales = request.env['garber.pets'].sudo().search([])
        else:
            # Buscar las mascotas asociadas con el usuario actual
            animales = request.env['garber.pets'].sudo().search([('asociacion', '=', user.id)])

        return http.request.render('adoptagarber.mascotas_table', {
            'mascotas': animales,
        })
    

    @http.route('/adopta-image', website=True, auth='public')
    def mostrarImagenes(self, **kw):
        mascotas = request.env['garber.pets'].sudo().search([])  

        return http.request.render('adoptagarber.mascotas_prueba', {
            'mascotas': mascotas,
        })
    
    @http.route('/adopta/<int:mascota_id>', type='http', auth='public', website=True)
    def mostrar_mascota(self, mascota_id):
        mascota = http.request.env['garber.pets'].sudo().browse(mascota_id)
        return http.request.render('adoptagarber.pet_single', {'mascota': mascota})
