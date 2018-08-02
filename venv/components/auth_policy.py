roles = [
    'admin',
    'reporter',
    'observer',
]

groups = {
    'admin_policy': ['admin'],
    'reporter_policy': ['reporter'],
    'observer_policy': ['observer']
}

permissions = {
    'admin_policy': {
        'version': '2018-07-31',
        'allow': {
            '/api/admin/*': ['*'],
        }
    },
    'reporter_policy': {
        'version': '2018-07-31',
        'allow': {
            '/api/user/{user_id:int}/credential':
                ['GET', 'PUT'],
            '/api/user/{user_id:int}/profile':
                ['POST', 'GET', 'PUT'],
            # user/workday
            '/api/user/{user_id:int}/workday':
                ['POST'],
            '/api/user/{user_id:int}/workday/{workday_id:int}':
                ['GET', 'PUT'],
            '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}}':
                ['GET', 'PUT'],
            '/api/user/{user_id:int}/workdays':
                ['GET', 'PUT'],
            # user/workday/note
            '/api/user/{user_id:int}/workday/{workday_id:int}/note':
                ['POST'],
            '/api/user/{user_id:int}/workday/{workday_id:int}/note/{note_id:int}':
                ['GET', 'PUT', 'DELETE'],
            '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}}/note/{note_id:int}':
                ['GET', 'PUT', 'DELETE'],
            '/api/user/{user_id:int}/workday/{workday_id:int}/notes':
                ['POST', 'GET', 'PUT', 'DELETE'],
            '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}}/notes':
                ['POST', 'GET', 'PUT', 'DELETE'],
            '/api/user/{user_id:int}/workday/{workday_id:int}/notes/{note_id:int}':
                ['GET', 'PUT', 'DELETE'],
            '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}}/notes/{note_id:int}':
                ['GET', 'PUT', 'DELETE'],
            # user/stint
            '/api/user/{user_id:int}/stint/{stint_id:int}':
                ['GET', 'PUT'],
            '/api/user/{user_id:int}/stints':
                ['GET'],
            '/api/user/{user_id:int}/stints/{stint_id:int}':
                ['GET', 'PUT'],
            # user/workday/stint
            '/api/user/{user_id:int}/workday/{workday_id:int}/stint':
                ['POST'],
            '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}}/stint':
                ['POST'],
            '/api/user/{user_id:int}/workday/{workday_id:int}/stints':
                ['GET', 'PUT'],
            '/api/user/{user_id:int}/workday/{start_time:dt("%Y-%m-%d")}}/stints':
                ['GET', 'PUT'],
            # user/workday/stint/note
            '/api/user/{user_id:int}/workdays/stint/{stint_id:int}/note':
                ['POST'],
            '/api/user/{user_id:int}/workdays/stint/{stint_id:int}/note/{note_id:int}':
                ['GET', 'PUT', 'DELETE'],
            '/api/user/{user_id:int}/workdays/{workday_id:int}/stints/{stint_id:int}/note':
                ['POST'],
            '/api/user/{user_id:int}/workdays/{workday_id:int}/stints/{stint_id:int}/note/{note_id:int}':
                ['GET', 'PUT', 'DELETE'],
            '/api/user/{user_id:int}/workdays/stints/{stint_id:int}/notes':
                ['POST'],
            '/api/user/{user_id:int}/workdays/stints/{stint_id:int}/notes/{note_id:int}':
                ['GET', 'PUT', 'DELETE'],
        }
    },
    'observer_policy': {
        # 'version': '2018-07-31',
        # 'allow': {'api/observer/*': ['GET']},
        # 'denny': {'*': ['POST', 'PUT', 'DELETE']}
    }
}