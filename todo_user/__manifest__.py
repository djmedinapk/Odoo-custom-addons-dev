# -*- coding: utf-8 -*-
{
    'name': "todo_user",

    'summary': "Multiusuario de la aplicacion To-Do, compartir tareas con tus companeros",

    'description': "Multiusuario To-Do",

    'author': "YoNo",
    'website': "To-do.com",
    'category': 'Events',
    'version': '0.1',

    'depends': ['todo_app','mail'],

    # always loaded
    'data': [
        'views/todo_task.xml',
    #    'security/ir.model.access.csv',
    #    'views/templates.xml',
    ],
}