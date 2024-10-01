from odoo import fields, models, api


class RealEstate(models.Model):
    _name = 'real.estate'
    _description = 'Vip'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    area = fields.Float(string='Area')
    rooms_ids = fields.One2many('room', 'real_estate_id', string='Rooms')
