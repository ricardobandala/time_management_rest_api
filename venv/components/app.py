from auth_policy import roles, groups, permissions
from auth import Authentication, Authorization
from content import ContentType
from db import Database
import falcon
# Resources for routes
from resource import user, identity


class App(falcon.API):

    def __init__(self):

        self.database_component = Database()
        self.content_type_component = ContentType(content_type='application/json')
        self.authenticate = Authentication(exempt_routes=['/login'], exempt_methods=['HEAD']).authenticate()
        self.authorize = Authorization(roles, groups, permissions)

        super().__init__(middleware=[
            self.database_component,
            self.content_type_component,
            self.authenticate,
            self.authorize
        ])

        self.add_route('/api/admin/user/', user.Item())
        self.add_route('/api/admin/user/{user_id:int}', user.Item())

        self.add_route('/api/admin/user/{user_id:int}/profile', identity.Item())
        self.add_route('/api/user/{user_id:int}/profile', identity.Item())


        # self.add_route('/api/user/profile/', user.Item())
        # self.add_route('/api/user/profile/{user_id:int}', user.Item())
        # self.add_route('/api/user/identity/{user_id:int}', user.Item())
        # self.add_route('/api/user/profile/identity/{user_id:int}', user.Item())

