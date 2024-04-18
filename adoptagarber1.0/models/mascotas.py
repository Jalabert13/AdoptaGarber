from datetime import datetime
from odoo import api, fields, models

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
    id = fields.Char(string="ID", required=True)
    image = fields.Image(string="Imagen", compute_sudo=True)
    edad = fields.Integer(string="Edad", compute='_compute_age')

    @api.depends('fecha_nac')
    def _compute_age(self):
        today = datetime.now().date()
        for pet in self:
            if pet.fecha_nac:
                delta = today - pet.fecha_nac
                pet.edad = delta.days // 365
            else:
                pet.edad = 0
