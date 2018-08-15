import datetime
"""
all length fields declared in minutes
all time fields declared in 24:00hrs format
"""
config = {
    'deltas': {
        'stint_length': 25,
        'workday_length': 480,
        'short_rest_length': 5,
        'long_rest_length': 10,
        'lunch_length': 30,
        'stint_interruptions_tolerance': 5, #Number of interruptions before declare an stint failed
    },
    'entities': {
        'stint': 'stint',
        'lunch': 'lunch',
        'short_rest': 'short_rest',
        'long_rest': 'long_rest'
    },
    'templates': {
        'workday':{
            'classic': {
            # TODO, implement this feature to check time validation on templates
            # 'valid_from' : ,
            # 'valid_until' :
                'structure': [
                    'stint', 'short_rest',
                    'stint', 'short_rest',
                    'stint', 'long_rest',
                    'stint', 'short_rest',
                    'stint', 'short_rest',
                    'stint', 'lunch',
                    'stint', 'short_rest',
                    'stint', 'short_rest',
                    'stint', 'long_rest',
                    'stint', 'short_rest',
                    'stint', 'short_rest',
                    'stint', 'long_rest',
                    'stint', 'short_rest',
                    'stint', 'short_rest',
                    'stint', 'long_rest',
            ]
            },
        },
    }
}