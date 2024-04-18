from requests import post
from odoo import http
from odoo.http import request


class Adopcion(http.Controller):

    
    @http.route('/adoptions', website=True, auth='public')
    def mostrarAnimalesFiltrados(self, **kw):
        clase = request.params.get('clase')
        raza = request.params.get('raza')
        sexo = request.params.get('sexo')

        # Verificar si al menos uno de los campos de filtro está presente
        if clase or raza or sexo:
            # Construir lista de dominios para aplicar los filtros
            domain = [('clase', 'ilike', clase)]
            if raza:
                domain.append(('raza', 'ilike', raza))
            if sexo:
                domain.append(('sexo', 'ilike', sexo))

            # Aplicar los filtros a la búsqueda en la base de datos
            animales = request.env['garber.pets'].sudo().search(domain)
        else:
            # Si no se proporcionan parámetros de filtro, obtener todas las mascotas
            animales = request.env['garber.pets'].sudo().search([])

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




    @http.route('/adopta-image', website=True, auth='public')
    def mostrarImagenes(self, **kw):
        mascotas = request.env['garber.pets'].sudo().search([])  

        return http.request.render('adoptagarber.mascotas_prueba', {
            'mascotas': mascotas,
        })
    
    @http.route('/adopta/<int:mascota_id>', type='http', auth='public', website=True)
    def mostrar_mascota(self, mascota_id):
        mascota = request.env['garber.pets'].sudo().browse(mascota_id)

        if not mascota:
            return """
                <html>
                    <head><title>Error</title></head>
                    <body>
                        <h1>Error: Mascota no encontrada</h1>
                        <p>Lo sentimos, No se ha encontrado ninguna mascota que corresponda a la búsqueda.</p>
                    </body>
                </html>
            """
        
        return http.request.render('adoptagarber.pet_single', {'mascota': mascota})