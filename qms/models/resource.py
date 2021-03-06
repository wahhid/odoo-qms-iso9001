# -*- coding: utf-8 -*-

from odoo import fields, models


class Resource(models.Model):

    _name = "qms.resource"

    _resource_types_ = [
        ('internal', 'Internal'),
        ('external', 'External')
    ]

    _resource_states_ = [
        ('available', 'Available'),
        ('in_process', 'In Process'),
        ('not_available', 'Not Available')
    ]

    name = fields.Char(
        required=True
    )

    resource_type = fields.Selection(
        selection=_resource_types_
    )

    state = fields.Selection(
        selection=_resource_states_,
        default='available'
    )
