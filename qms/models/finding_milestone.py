# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Finding_Milestone(models.Model):

    _name = 'qms.finding.milestone'
    _order = 'sequence'

    name = fields.Char(
        required=True,
        translate=True
    )

    description = fields.Text()

    sequence = fields.Integer()

    parent_left = fields.Integer(
        index=True
    )

    parent_right = fields.Integer(
        index=True
    )

    reference_code = fields.Char()

    @api.multi
    def name_get(self):
        res = []
        for obj in self:
            name = obj.name
            if obj.parent_id:
                name = obj.parent_id.name_get()[0][1] + ' / ' + name
            res.append((obj.id, name))
        return res
