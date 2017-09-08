# -*- coding: utf-8 -*-

from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    analytic_id = fields.Many2one("account.analytic.account")
