from datetime import datetime
from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import content_disposition, dispatch_rpc, request, Response
from odoo import api, fields, models
import logging

logger = logging.getLogger(__name__)

class Mascotas(models.Model):
    _name = "garber.pets"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Registro de mascotas"

    name = fields.Char(string="Nombre", required=True)
    breed = fields.Char(string="Raza")
    pet_class = fields.Char(string="Clase")
    size = fields.Selection([('pequeño', 'Pequeño'), ('mediano', 'Mediano'), ('grande', 'Grande')], string="Tamaño")
    entry_date = fields.Date(string="Fecha de Ingreso")
    sex = fields.Selection([('macho', 'Macho'), ('hembra', 'Hembra')], string="Sexo")
    weight = fields.Float(string="Peso")
    height = fields.Float(string="Altura")
    location = fields.Char(string="Localidad")
    birth_date = fields.Date(string="Fecha de Nacimiento")
    image = fields.Image(string="Imagen", compute_sudo=True)
    age = fields.Char(string="Edad", compute='_compute_age')
    asociation = fields.Many2one('res.users', string="Asociación", readonly=True, default=lambda self: self.env.user)
    description = fields.Text(string="Descripcion")
    contact_phone = fields.Char(string="Telefono de contacto")
    state = fields.Selection([('available', 'Disponible'),
                              ('in_process', 'En proceso'),
                               ('adopted', 'Adoptado')], default='available' ,string = "Estado de la Adopción")


    @api.depends('birth_date')
    def _compute_age(self):
        today = datetime.now().date()
        for pet in self:
            if pet.birth_date:
                delta = today - pet.birth_date
                years = delta.days // 365
                months = delta.days % 365 // 30
                days = delta.days % 30
                if years < 1:
                    if months == 0:
                        pet.age = "{} días".format(days)
                    else:
                        pet.age = "{} meses y {} días".format(months, days)
                else:
                    pet.age = "{} años".format(years)
            else:
                pet.age = "Desconocido"

    @api.model
    def action_view_pet(self, id):
        id = str(id).strip('[]')
        
        target_url = f"http://192.168.100.85:8070/adopta/{id}"

        logger.info("Redirigiendo a: %s", target_url)
        
        return {
            'type': 'ir.actions.act_url',
            'url': target_url,
            'target': 'self',
        }
    
    def action_share_whatsapp(self):
        if not self.contact_phone:
            raise ValidationError("No hay telefono de contacto para la mascota")
        
        msg = f"Hola {self.asociation.name}, dueño temporal de {self.name}"
        api_whatsapp = "https://api.whatsapp.com/send?phone=%s&text=%s" % (self.contact_phone, msg)
        
        return {
            'type': 'ir.actions.act_url',
            'url': api_whatsapp,
            'target': 'new'
        }
