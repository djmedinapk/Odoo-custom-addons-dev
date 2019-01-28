# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']
    user_id = fields.Many2one('res.users','Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="Que necesitas para acabar?")

    @api.multi
    def do_clear_done(self):
        domain = [('is_done', '=', True),
                '|', ('user_id', '=', self.env.uid),
                        ('user_id', '=', False)]
        dones = self.search(domain)
        dones.write({'active': False})
        return True
        
    @api.multi 
    def do_toggle_done(self):
        for task in self:
            if task.user_id != self.env.user:
                raise ValidationError('Only the responsible can do this!')
        return super(TodoTask, self).do_toggle_done()

# class todo_user(models.Model):
#     _name = 'todo_user.todo_user'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100