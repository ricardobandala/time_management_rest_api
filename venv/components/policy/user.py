routes = {
        '/api/user/': {
            'POST': ['general_management']
        },
        '/api/user/{user_id:int}': {
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'DELETE': ['general_management']
        },
        '/api/users/': {
            'GET': ['general_management'],
            'POST': ['general_management'],
            'DELETE': ['general_management']
        },
        '/api/user/{user_id:int}/credential': {
            'POST': ['general_management'],
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['general_management']
        },
        '/api/users/credentials': {
            'POST': ['general_management'],
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'PATCH': ['general_management'],
            'DELETE': ['general_management']
        },
        # Profile is the repr of the `identity` Object
        '/api/user/{user_id:int}/profile': {
            'POST': ['general_management'],
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['general_management']
        },
        '/api/users/profiles': {
            'POST': ['general_management'],
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'PATCH': ['self_management'],
            'DELETE': ['general_management']
        },
        # Hole user/credential/identity entity
        '/api/user/{user_id:int}/aggregate': {
            'POST': ['general_management'],
            'GET': ['self_management'],
            'PUT': ['self_management']
        },
        '/api/users/aggregate': {
            'POST': ['general_management'],
            'GET': ['self_management'],
            'PUT': ['self_management']
        },
        # WORKDAY
        '/api/user/{user_id:int}/workday': {
            'POST': ['self_management'],
        },
        '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%dT%H:%M:%SZ")}': {
            'POST': ['general_management'],
        },
        '/api/user/{user_id:int}/workday/{workday_id:int}}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['general_management']
        },
        '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['general_management']
        },
        '/api/user/{user_id:int}/workdays': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['general_management']
        },
        '/api/users/workdays': {
            'POST': ['general_management'],
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'DELETE': ['general_management']
        },
        # WORKDAY NOTES
        '/api/user/{user_id:int}/workday/{workday_id:int}/note': {
            'POST': ['self_management'],
        },
        '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%dT%H:%M:%SZ")}/note': {
            'POST': ['general_management'],
        },
        '/api/user/{user_id:int}/workday/{workday_id:int}/note/{note_id:int}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['self_management']
        },
        '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}/note/{note_id:int}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['self_management']
        },
        '/api/user/{user_id:int}/workday/{workday_id:int}/notes': {
            'POST': ['self_management'],
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['self_management']
        },
        '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}/notes': {
            'POST': ['self_management'],
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['self_management']
        },
        '/api/users/workdays/notes': {
            'POST': ['general_management'],
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'DELETE': ['general_management']
        },
        # STINT
        '/api/user/{user_id:int}/stint': {
            'POST': ['self_management'],
        },
        '/api/user/{user_id:int}/stint/{stint_id:int}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['general_management']
        },
        '/api/user/{user_id:int}/stints': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['general_management']
        },
        '/api/users/stints': {
            'POST': ['general_management'],
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'DELETE': ['general_management']
        },
        # STINT NOTES
        '/api/user/{user_id:int}/stint/{stint_id:int}/note': {
            'POST': ['self_management'],
        },
        '/api/user/{user_id:int}/stint/{start_time:dt("%Y-%m-%dT%H:%M:%SZ")}/note': {
            'POST': ['general_management'],
        },
        '/api/user/{user_id:int}/stint/{stint_id:int}/note/{note_id:int}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['self_management']
        },
        '/api/user/{user_id:int}/stint/{start_time:dt("%Y-%m-%d")}/note/{note_id:int}': {
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['self_management']
        },
        '/api/user/{user_id:int}/stint/{stint_id:int}/notes': {
            'POST': ['self_management'],
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['self_management']
        },
        '/api/user/{user_id:int}/stint/{start_time:dt("%Y-%m-%d")}/notes': {
            'POST': ['self_management'],
            'GET': ['self_management'],
            'PUT': ['self_management'],
            'DELETE': ['self_management']
        },
        '/api/users/stints/notes': {
            'POST': ['general_management'],
            'GET': ['general_management'],
            'PUT': ['general_management'],
            'DELETE': ['general_management']
        }
}
