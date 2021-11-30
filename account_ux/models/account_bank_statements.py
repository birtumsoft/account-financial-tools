##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class AccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    move_name = fields.Char(compute='compute_move_name', string='Journal Entry', readonly=True)

    def compute_move_name(self):
        for rec in self:
            rec.move_name = rec.line_ids.mapped('move_id.name')

    def cancel_all_lines(self):
        for rec in self:
            rec.line_ids.filtered('journal_entry_ids').button_cancel_reconciliation()
        return True
