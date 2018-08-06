from auth import Authentication, Authorization, TokenHandler, Permission
from content import ContentType
from db import Database
import falcon
from auth_policy import roles as app_roles, groups as app_groups, permissions as app_permissions
# Resources for routes
from resource import user, identity, login, wala


class App(falcon.API):

    def __init__(self):
        self.authenticate_route = '/api/login'
        self.database_component = Database()
        self.content_type_component = ContentType(content_type='application/json')
        self.authenticate = Authentication()
        self.permission = Permission(
                roles=app_roles,
                groups=app_groups,
                permissions=app_permissions
        )
        self.token_handler = TokenHandler(
                login_route=self.authenticate_route,
                key='Camouflaged by insecurities, blinded by it all.',
                headers={"alg": "HS256", "typ": "JWT"},
                minutes_lifespan=60,
                permission_handler=self.permission
        )
        self.authorize = Authorization(
            app_permissions,
            exempt_routes=[
                self.authenticate_route
            ]
        )

        super().__init__(middleware=[
            self.database_component,
            self.content_type_component,
            self.authenticate,
            self.token_handler,
            self.authorize
        ])

        self.add_route(self.authenticate_route, login.LoginItem())

        self.add_route('/api/admin/user/', user.Item())
        self.add_route('/api/admin/user/{user_id:int}', user.Item())
        self.add_route('/api/admin/user/{user_id:int}/profile', identity.Item())

        self.add_route('/api/user/profile', identity.Item())
        self.add_route('/api/user/credential', wala.Item())

        self.add_route('/api/user/workday', wala.Item())
        self.add_route('/api/user/workday/{workday_id:int}', wala.Item())
        self.add_route('/api/user/workday/{start_time:dt("%Y-%m-%d")}}', wala.Item())
        self.add_route('/api/user/workdays', wala.Collection())

        self.add_route('/api/user/workday/{workday_id:int}/note', wala.Item())
        self.add_route('/api/user/workday/{workday_id:int}/note/{note_id:int}', wala.Item())
        self.add_route('/api/user/workday/{start_time:dt("%Y-%m-%d")}}/note/{note_id:int}', wala.Item())
        self.add_route('/api/user/workday/{workday_id:int}/notes', wala.Collection())
        self.add_route('/api/user/workday/{start_time:dt("%Y-%m-%d")}}/notes', wala.Collection())
        self.add_route('/api/user/workday/{workday_id:int}/notes/{note_id:int}', wala.Collection())
        self.add_route('/api/user/workday/{start_time:dt("%Y-%m-%d")}}/notes/{note_id:int}', wala.Collection())

        self.add_route('/api/user/stint/{stint_id:int}', wala.Item())
        self.add_route('/api/user/stints', wala.Collection())
        self.add_route('/api/user/stints/{stint_id:int}', wala.Item())
        self.add_route('/api/user/workday/{workday_id:int}/stint', wala.Item())
        self.add_route('/api/user/workday/{start_time:dt("%Y-%m-%d")}}/stint', wala.Item())
        self.add_route('/api/user/workday/{workday_id:int}/stints', wala.Collection())
        self.add_route('/api/user/workday/{start_time:dt("%Y-%m-%d")}}/stints', wala.Collection())

        self.add_route('/api/user/workdays/stint/{stint_id:int}/note', wala.Item())
        self.add_route('/api/user/workdays/stint/{stint_id:int}/note/{note_id:int}', wala.Item())
        self.add_route('/api/user/workdays/{workday_id:int}/stints/{stint_id:int}/note', wala.Item())
        self.add_route('/api/user/workdays/{workday_id:int}/stints/{stint_id:int}/note/{note_id:int}', wala.Item())
        self.add_route('/api/user/workdays/stints/{stint_id:int}/notes', wala.Collection())
        self.add_route('/api/user/workdays/stints/{stint_id:int}/notes/{note_id:int}', wala.Item())

