import falcon
from content import ContentType
from db import Database
from auth import Authentication, Authorization
# Resources for routes
from resource import user


class App(falcon.API):

    def __init__(self):

        self.database_component = Database()
        self.content_type_component = ContentType(content_type='application/json')
        self.authenticate = Authentication(exempt_routes=['/login'], exempt_methods=['HEAD']).authenticate()
        self.authorize = Authorization()

        super().__init__(middleware=[
            self.database_component,
            self.content_type_component,
            self.authenticate,
            self.authorize
        ])

        self.add_route('/user/{user_id:int}', user.Item())
        self.add_route('/user/', user.Item())
