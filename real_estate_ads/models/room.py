from odoo import fields, models, api


class Room(models.Model):
    _name = 'room'
    _description = 'Room'

    name = fields.Char()
    real_estate_id = fields.Many2one('real.estate')
    room_type_id = fields.Many2one('room.type', readonly=True)
    area = fields.Float()
    price = fields.Float(string='Price')
