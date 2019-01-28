# -*- coding: utf-8 -*- 
from odoo import models, fields, api
class TodoTask(models.Model): 
    _name = 'todo.task' 
    _description = 'Tareas por hacer'
    name = fields.Char('Descripcion', required=True) 
    is_done = fields.Boolean('Teminada?') 
    active = fields.Boolean('Activa?', default=True)
    @api.multi 
    def do_toggle_done(self): 
        for task in self:
            task.is_done = not task.is_done 
            #if task.is_done:
                #task.active = False
            #else:
                #task.active = True
        return True
        
    @api.multi 
    def do_clear_done(self): 
        dones = self.search([('is_done','=', True)]) 
        dones.write({'active': False}) 
        return True