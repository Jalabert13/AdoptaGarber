import base64
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
    size = fields.Selection([('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')], string="Tamaño")
    entry_date = fields.Date(string="Fecha de Ingreso")
    sex = fields.Selection([('Macho', 'Macho'), ('Hembra', 'Hembra')], string="Sexo")
    weight = fields.Float(string="Peso")
    height = fields.Float(string="Altura")
    location = fields.Char(string="Localidad")
    birth_date = fields.Date(string="Fecha de Nacimiento")
    image = fields.Image(string="Imagen", compute_sudo=True, compute="_compute_image")
    age = fields.Char(string="Edad", compute='_compute_age')
    asociation = fields.Many2one('res.users', string="Asociación", readonly=True, default=lambda self: self.env.user)
    description = fields.Text(string="Descripcion")
    contact_phone = fields.Char(string="Telefono de contacto")
    image_path = fields.Char(string="Ruta de la imagen")
    state = fields.Selection([('available', 'Disponible'),
                              ('in_process', 'En proceso'),
                               ('adopted', 'Adoptado')], default='available', string = "Estado de la Adopción")
    image_ids = fields.One2many('pet.image', 'pet_id', string='Images')

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


    @api.depends('image_path')
    def _compute_image(self):
        for record in self:
            if record.image_path:
                with open(record.image_path, 'rb') as img:
                    image_data = base64.b64encode(img.read())
                    record.image = image_data

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
    
    def action_invoice_sent(self):
        """ Open a window to compose an email, with the edi invoice template
            message loaded by default
        """
        self.ensure_one()

        report_action = self.action_send_and_print()
        if self.env.is_admin() and not self.env.company.external_report_layout_id and not self.env.context.get('discard_logo_check'):
            return self.env['ir.actions.report']._action_configure_external_report_layout(report_action)

        return report_action
    
    def print_pdf(self):
        report = self.env.ref('adoptagarber.report_garber_pets_card').report_action(self)
        return report
        
