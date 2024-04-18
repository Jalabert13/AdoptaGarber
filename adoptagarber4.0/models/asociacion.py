from odoo import api, fields, models

import logging

logger = logging.getLogger(__name__)

class Asociacion(models.Model):
    _name = 'garber.asociacion'
    _description = "Información del contacto que tiene el Animal"

    name = fields.Char(string="Nombre", required=True)
    localidad = fields.Char(string="Localidad")
    municipio = fields.Char(string="Municipio")
    telefono_contacto = fields.Char(string="Telefono de contacto")
    mascotas_ids = fields.One2many('garber.pets', 'asociacion_id', string="Lista de Mascotas")
