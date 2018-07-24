policy_config = {

    'roles': [
        'admin',
        'reporter',
        'observer',
    ],

    'groups': {
        'general_management': ['admin'],
        'self_management': ['admin', 'reporter'],

        'create': ['admin', 'reporter'],
        'update': ['admin', 'reporter'],
        'read': ['admin', 'reporter', 'observer'],
        'delete': ['admin'],
    },

    'routes': {
        # TODO, implement toke generator
        # '/login': {
        #     'POST': ['@passthrough'],
        # },
        '/user/': {
            'POST': ['general_management'],
        },
        '/user/{user_id:int}': {
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'PATCH': ['general_management'],
            'DELETE': ['general_management'],
        },
        '/credential/own/{user_id:int}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'PATCH': ['self_management'],
        },
        '/credential/{user_id:int}': {
            'POST': ['general_management'],
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'PATCH': ['general_management'],
            'DELETE': ['general_management'],
        },
        # Profile is the repr of the `identity` Object
        '/profile/own/{user_id:int}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'PATCH': ['self_management']
        },
        '/profile/{user_id:int}': {
            'POST': ['@any_role'],
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'PATCH': ['self_management'],
            'DELETE': ['general_management'],
        },
        # '/timeframe/': {
        #     'POST': ['@any_role'],
        # },
        # '/timeframe/own/{user_id:int}': {
        #     'GET': ['self_management'],
        #     'PUT': ['self_management'],
        #     'PATCH': ['self_management']
        # },
        # '/timeframe/{user_id:int}': {
        #     'GET': ['general_management'],
        #     'PUT': ['general_management'],
        #     'PATCH': ['general_management'],
        #     'DELETE': ['general_management'],
        # },
        # '/timeframe-note/{user_id:int}/': {
        #     'POST': ['@any_role'],
        # },
        # '/timeframe-note/own/{user_id:int}': {
        #     'GET': ['self_management'],
        #     'PUT': ['self_management'],
        #     'PATCH': ['self_management']
        # },
        # '/timeframe-note/{user_id:int}': {
        #     'GET': ['general_management'],
        #     'PUT': ['general_management'],
        #     'PATCH': ['general_management'],
        #     'DELETE': ['general_management'],
        # }
    },
}

# policy_config = {
#     'roles': [
#         'admin',
#         'creator',
#         'observer',
#     ],
#     'groups': {
#         'create': ['admin', 'creator'],
#         'update': ['admin', 'creator'],
#         'read': ['admin', 'creator', 'observer'],
#         'delete': ['admin'],
#     },
#     'routes': {
#         '/quote': {
#             'GET': ['read'],
#             'POST': ['create'],
#             'PUT': ['update'],
#             'DELETE': ['delete'],
#         },
#         '/quote/{id}': {
#             'GET': ['read'],
#             'POST': ['create'],
#             'PUT': ['update'],
#             'DELETE': ['delete'],
#         },
#         '/status': {
#             'GET': ['@any-role'],
#             'HEAD': ['@passthrough'],
#         },
#     },
# }