from datetime import datetime
from odoo import http
from odoo.http import content_disposition, dispatch_rpc, request, Response
from odoo import api, fields, models
import logging

logger = logging.getLogger(__name__)

class Mascotas(models.Model):
    _name = "garber.pets"
    _description = "Registro de mascotas"

    name = fields.Char(string="Nombre", required=True)
    raza = fields.Char(string="Raza")
    clase = fields.Char(string="Clase")
    tamanyo = fields.Char(string="Tamaño")
    fecha_ingreso = fields.Date(string="Fecha de Ingreso")
    sexo = fields.Selection([('macho', 'Macho'), ('hembra', 'Hembra')], string="Sexo")
    peso = fields.Float(string="Peso")
    altura = fields.Float(string="Altura")
    localidad = fields.Char(string="Localidad")
    fecha_nac = fields.Date(string="Fecha de Nacimiento")
    id = fields.Char(string="ID", required=True, copy=False)
    image = fields.Image(string="Imagen", compute_sudo=True)
    edad = fields.Char(string="Edad", compute='_compute_age')
    asociacion = fields.Many2one('res.users', string="Asociación", readonly=True, default=lambda self: self.env.user)
    descripcion = fields.Text(string="Descripcion")

    @api.depends('fecha_nac')
    def _compute_age(self):
        today = datetime.now().date()
        for pet in self:
            if pet.fecha_nac:
                delta = today - pet.fecha_nac
                years = delta.days // 365
                months = delta.days % 365 // 30
                days = delta.days % 30
                if years < 1:
                    if months == 0:
                        pet.edad = "{} días".format(days)
                    else:
                        pet.edad = "{} meses y {} días".format(months, days)
                else:
                    pet.edad = "{} años".format(years)
            else:
                pet.edad = "Desconocido"

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
    
    
