{
    'name': 'Modulo de Garber para adopción de mascotas',
    'author': 'Garber Web Solutions S.L.',
    'website': 'https://www.garber.es/',
    'summary': 'Sistema de Gestion de adopciones de Garber.',
    'depends' : ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mascotas.xml',
        'views/template.xml',
        'views/filtro.xml',
        # 'views/print_pdf.xml',

        # 'report/report.xml',
        # 'report/report_pet.xml',
        'data/garber_pets_data.xml',
        'data/garber.pets.csv',
        
    ],
    'assets': {
        'web.assets_frontend': [
            'adoptagarber/static/src/js/prueba.js',
            'adoptagarber/static/src/js/expand_image.js',
            'adoptagarber/static/src/js/change_image.js',
            # 'adoptagarber/static/src/js/single_pet_form.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}