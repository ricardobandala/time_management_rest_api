from user import routes as user_routes


roles = [
        'admin',
        'reporter',
        'observer',
]

groups = {
    'general_management': ['admin'],
    'self_management': ['admin', 'reporter'],

    'create': ['admin', 'reporter'],
    'update': ['admin', 'reporter'],
    'read': ['admin', 'reporter', 'observer'],
    'delete': ['admin'],
}

routes = {
    '/login': {
        'POST': ['@passthrough'],
    },
}
routes.update(user_routes)

policy_definition = {'roles': roles, 'groups': groups, 'routes': routes}
