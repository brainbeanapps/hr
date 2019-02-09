# Copyright 2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HrLeaveSummaryWizard(models.TransientModel):
    _name = 'hr.leave.summary.wizard'
    _description = 'HR Leave Summary Wizard'

    date = fields.Date(
        string='Date',
        required=True,
    )

    @api.multi
    def action_generate(self):
        self.ensure_one()

        # TODO: action to open a generated TREE of models, thus model ids
        return {

        }