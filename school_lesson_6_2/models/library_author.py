import datetime
from odoo import fields, models


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(
        required=True,
        translate=True,
    )
    last_name = fields.Char(
        required=True,
        translate=True,
    )
    birth_date = fields.Date('Birthday')

    can_edit_by_trainee = fields.Boolean(
        compute='_compute_is_old',
        # store=True,
    )

    def name_get(self):
        return [(rec.id, "%s %s" % (
            rec.first_name, rec.last_name)) for rec in self]

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)

    def _compute_is_old(self):
        date_min = datetime.datetime.now() - datetime.timedelta(days=30)
        for author in self:
            if author.create_date:
                author.can_edit_by_trainee = author.create_date >= date_min
            else:
                author.can_edit_by_trainee = False
