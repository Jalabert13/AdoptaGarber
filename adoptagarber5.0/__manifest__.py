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
    ],
    'assets': {
        'web.assets_frontend': [
            'adoptagarber/static/src/js/prueba.js',
        ],
    },
}