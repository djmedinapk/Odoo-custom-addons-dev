{ 
    'name': 'To-Do Application', 
    'description': 'Maneja tus tareas.', 
    'author': 'Daniel Reis - djmedina', 
    'depends': ['base'], 
    'data': [
        'security/todo_access_rules.xml',
        'security/ir.model.access.csv',
        'views/todo_menu.xml',
        'views/todo_view.xml',
    ],
    'application': True, 
    
}