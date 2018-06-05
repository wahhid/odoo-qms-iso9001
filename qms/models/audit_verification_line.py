# -*- coding: utf-8 -*-
# This model is based in some code used in OCA Management System Addons Project
# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Audit_Verification_Line(models.Model):

    _name = "qms.audit.verification.line"
    _order = "seq"

    name = fields.Char(
        string='Question',
        required=True
    )

    point_norm = fields.Char(
        string='Point of the norm',
        required=True
    )

    audit_id = fields.Many2one(
        comodel_name='qms.audit',
        ondelete='cascade',
        index=True
    )

    is_conformed = fields.Boolean()

    comments = fields.Text()

    seq = fields.Integer(
        string='Sequence'
    )
