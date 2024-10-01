from odoo import fields, models, api


class RoomType(models.Model):
    _name = 'room.type'
    _description = 'Room Type'

    name = fields.Char()
    description = fields.Text()
