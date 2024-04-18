from requests import post
from odoo import http
from odoo.http import request


class Adopcion(http.Controller):

    @http.route('/adoptions', website=True, auth='public')
    def mostrarAnimalesFiltrados(self, **kw):
        pet_class = request.params.get('pet_class')
        breed = request.params.get('breed')
        sex = request.params.get('sex')

        domain = []
        if pet_class:
            domain.append(('pet_class', 'ilike', pet_class))
        if breed:
            domain.append(('breed', 'ilike', breed))
        if sex:
            domain.append(('sex', 'ilike', sex))

        animals = request.env['garber.pets'].sudo().search(domain)

        # Obtener valores únicos para las opciones del select
        all_animals = request.env['garber.pets'].sudo().search([])
        # pet_classes = set(all_animals.mapped('pet_class'))

        #COMPRUEBA QUE NO HAYA CAMPOS VACIOS Y DISTINGUE ENTRE MAYUSCULAS Y MINUSCULAS
        pet_classes = {animal.pet_class.strip().lower() for animal in all_animals if isinstance(animal.pet_class, str) and animal.pet_class.strip()}
        breeds = {breed.strip().lower() for breed in all_animals.mapped('breed') if isinstance(breed, str) and breed.strip()}

        return http.request.render('adoptagarber.filtro_busqueda_animales', {
            'animals': animals,
            'pet_classes': pet_classes,
            'breeds': breeds,
            'selected_pet_class': pet_class,
            'selected_breed': breed,
            'sex': sex,
        })

    @http.route('/adopt-image', website=True, auth='public')
    def show_images(self, **kw):
            pets = request.env['garber.pets'].sudo().search([])  

            return http.request.render('adoptagarber.mascotas_prueba', {
                'mascotas': pets,
            })

    
        
    @http.route('/adopta/<int:mascota_id>', type='http', auth='public', website=True)
    def mostrar_mascota(self, mascota_id):
            pet = request.env['garber.pets'].sudo().browse(mascota_id)

            if not pet:
                return """
                    <html>
                        <head><title>Error</title></head>
                        <body>
                            <h1>Error: Mascota no encontrada</h1>
                            <p>Lo sentimos, No se ha encontrado ninguna mascota que corresponda a la búsqueda.</p>
                        </body>
                    </html>
                """
            
            return http.request.render('adoptagarber.pet_single', {'mascota': pet})