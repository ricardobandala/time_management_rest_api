import falcon
from content import ContentType
from db import Database
from auth import auth
# Resources for routes
from resource import user


class App(falcon.API):

    def __init__(self):

        self.database_component = Database()
        self.content_type_component = ContentType(content_type='application/json')
        # TODO, add init parameters to config exemtions here
        # self.auth = Auth(exempt_routes=['/login']).auth
        self.auth = auth

        super().__init__(middleware=[
            self.database_component,
            self.content_type_component,
            self.auth
        ])

        self.add_route('/user/{user_id:int}', user.Item())
