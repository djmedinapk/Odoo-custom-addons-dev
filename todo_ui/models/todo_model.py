# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Tags(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-Do Etiquetas'
    _parent_store = True
    name = fields.Char('Name')
    parent_id = fields.Many2one('todo.task.tag','Parent Tag',ondelete='restrict')
    parent_left = fields.Integer('parent Left', index=True)
    parent_right = fields.Integer('parent Right', index=True)
    

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-Do Etapas'
    _order = 'sequence,name'
    name = fields.Char('Name')
    desc = fields.Text('Description')
    state = fields.Selection([('draft','New'),('open','Started'),('done','Closed')],'State')
    docs  = fields.Html('Documentation')
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete',(3,2))
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')
    tasks = fields.One2many('todo.task','stage_id','Tasks in this stage')

class TodoTask(models.Model):
    _inherit = 'todo.task'
    stage_id = fields.Many2one('todo.task.stage','Stage')
    tag_ids = fields.Many2many('todo.task.tag',string='Tags')
    refers_to = fields.Reference([('res.user','User'),('res.partner','Partner')],'Refers to')
    stage_fold = fields.Boolean('Satge Folded?',compute='_compute_stage_fold',search='_search_stage_fold',inverse='_write_stage_fold')
    stage_state = fields.Selection(related='stage_id.state',string='Stage State')
    _sql_constraints = [('todo_task_name_iniq','UNIQUE(name,active)','Task title must be unique!')]
    effort_estimate = fields.Integer('Effort Estimate')

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold
    
    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold
    
    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise exceptions.ValidationError('Debe Contener almenos 5 Caracteres!')
    
    def compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count([('user_id','=','task.user_id.id')])
    
    user_todo_count = fields.Integer('User To-Do Count',compute='compute_user_todo_count')


