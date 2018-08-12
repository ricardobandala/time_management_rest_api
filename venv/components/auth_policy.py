roles = [
    'admin',
    'reporter',
    'observer',
]

groups = {
    'admin_policy': ['admin'],
    'reporter_policy': ['reporter'],
    'observer_policy': ['observer'],
    'post_with_id': ['admin']
}

permissions = {
    'admin_policy': {
        'version': '2018-07-31',
        'allow': {
            '^(\/api\/admin\/)?': ['*'],
        }
    },
    'reporter_policy': {
        'version': '2018-07-31',
        'allow': {
            '^(\/api\/user\/credential)$':
                ['GET', 'PUT'],
            '^(\/api\/user\/profile)$':
                ['POST', 'GET', 'PUT'],
            # user\/workday
            '^(\/api\/user\/workday)$':
                ['POST'],
            '^(\/api\/user\/workday\/{workday_id:int})$':
                ['GET', 'PUT'],
            '^(\/api\/user\/workday\/{start_time:dt("%Y-%m-%d")})$':
                ['GET', 'PUT'],
            '^(\/api\/user\/workdays)$':
                ['GET', 'PUT'],
            # user\/workday\/note
            '^(\/api\/user\/workday\/{workday_id:int}\/note)$':
                ['POST'],
            '^(\/api\/user\/workday\/{workday_id:int}\/note\/{note_id:int})$':
                ['GET', 'PUT', 'DELETE'],
            '^(\/api\/user\/workday\/{start_time:dt("%Y-%m-%d")}\/note\/{note_id:int})$':
                ['GET', 'PUT', 'DELETE'],
            '^(\/api\/user\/workday\/{workday_id:int}\/notes)$':
                ['POST', 'GET', 'PUT', 'DELETE'],
            '^(\/api\/user\/workday\/{start_time:dt("%Y-%m-%d")}\/notes)$':
                ['POST', 'GET', 'PUT', 'DELETE'],
            '^(\/api\/user\/workday\/{workday_id:int}\/notes\/{note_id:int})$':
                ['GET', 'PUT', 'DELETE'],
            '^(\/api\/user\/workday\/{start_time:dt("%Y-%m-%d")}\/notes\/{note_id:int})$':
                ['GET', 'PUT', 'DELETE'],
            # user\/stint
            '^(\/api\/user\/stint\/{stint_id:int})$':
                ['GET', 'PUT'],
            '^(\/api\/user\/stints)$':
                ['GET'],
            '^(\/api\/user\/stints\/{stint_id:int})$':
                ['GET', 'PUT'],
            # user\/workday\/stint
            '^(\/api\/user\/workday\/{workday_id:int}\/stint)$':
                ['POST'],
            '^(\/api\/user\/workday\/{start_time:dt("%Y-%m-%d")}\/stint)$':
                ['POST'],
            '^(\/api\/user\/workday\/{workday_id:int}\/stints)$':
                ['GET', 'PUT'],
            '^(\/api\/user\/workday\/{start_time:dt("%Y-%m-%d")}\/stints)$':
                ['GET', 'PUT'],
            # user\/workday\/stint\/note
            '^(\/api\/user\/workdays\/stint\/{stint_id:int}\/note)$':
                ['POST'],
            '^(\/api\/user\/workdays\/stint\/{stint_id:int}\/note\/{note_id:int})$':
                ['GET', 'PUT', 'DELETE'],
            '^(\/api\/user\/workdays\/{workday_id:int}\/stints\/{stint_id:int}\/note)$':
                ['POST'],
            '^(\/api\/user\/workdays\/{workday_id:int}\/stints\/{stint_id:int}\/note\/{note_id:int})$':
                ['GET', 'PUT', 'DELETE'],
            '^(\/api\/user\/workdays\/stints\/{stint_id:int}\/notes)$':
                ['POST'],
            '^(\/api\/user\/workdays\/stints\/{stint_id:int}\/notes\/{note_id:int})$':
                ['GET', 'PUT', 'DELETE'],
        }
    },
    'observer_policy': {
        # 'version': '2018-07-31',
        # 'allow': {'api\/observer\/*': ['GET']},
        # 'denny': {'*': ['POST', 'PUT', 'DELETE']}
    },
    'post_with_id': {
        'version': '2018-08-09',
        'deny': {
            '(\/user\/{user_id:int})$': #'^(\/api\/admin\/user\/{user_id:int)$}'
                ['POST'],
            '(\/workday\/{workday_id:int})$':
                ['POST'],
            '(\/stint\/{stint_id:int})$':
                ['POST'],
            '(\/note\/{note_id:int})$':
                ['POST']
        }
    }
}