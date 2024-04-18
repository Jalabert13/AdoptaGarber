from odoo import models, fields

class PetImage(models.Model):
    _name = 'pet.image'
    _description = 'Pet Image'

    name = fields.Char(string='Name')
    image = fields.Binary(string='Image')
    pet_id = fields.Many2one('garber.pets', string='Pet')