from odoo import models, _


class LibraryBookCategory(models.Model):
    """
    Books categories, inherit from school_lessons_6_1
    """
    _inherit = 'library.book.category'

    def action_book_list(self):
        """
        Open selected category books
        """
        self.ensure_one()
        return {
            'name': _('Category Books'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'library.book',
            'context': {'default_category_id': self.id},
            'domain': [('category_id', '=', self.id)],
        }
