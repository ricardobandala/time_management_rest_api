import base64
from db import Database
import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend
from sqlalchemy.orm import joinedload, raiseload
from model.user import UserModel
from model.credential import CredentialModel

session = Database().Session()


def session_handler(f):
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        finally:
            session.close()
        return result

    return wrapper


class Authentication(object):
    exempt_routes = None
    exempt_methods = None

    def __init__(self, exempt_routes: list, exempt_methods: list):
        self.exempt_routes = exempt_routes
        self.exempt_methods = exempt_methods
        pass

    def authenticate(self):

        @session_handler
        def user_loader(username: str, password: str):

            credential = session.query(CredentialModel.user_id).filter(
                CredentialModel.username == username,
                CredentialModel.password == base64.b64encode(password.encode('utf-8'))
            ).options(raiseload('*')).one()

            return credential

        return FalconAuthMiddleware(
            BasicAuthBackend(user_loader),
            self.exempt_routes,
            self.exempt_methods
        )


class Authorization(object):
    def __init__(self, roles, groups, permissions):
        self.roles = roles
        self.groups = groups
        self.permissions = permissions

    def process_resource(self, req, resp, resource, params):

        query = req.context['session'].query(UserModel)
        query = query.options(joinedload('role'), raiseload('*'))

        user = query.filter(
            UserModel.id == req.context['user'].user_id
        ).one()

        if user:
            self.screen(user.get_role(), req.uri_template, req.method)
        else:
            falcon.HTTPForbidden()

    def screen(self, user_role: list, uri_template: str, request_method: str):

        user_group = self.get_role_group(user_role)
        if not user_group:
            falcon.HTTPForbidden()
            pass

        user_permissions = self.get_group_permissions(user_group)
        if not user_permissions:
            falcon.HTTPForbidden()
            pass

        if not self.test_permissions(user_permissions, uri_template, request_method):
            falcon.HTTPForbidden()

    def get_role_group(self, user_role: list):

        intersection = list(set(user_role) & set(self.roles))

        if not intersection:
            falcon.HTTPForbidden()
        else:
            return [k for k, v in self.groups.items() if list(set(v) & set(intersection))]

    def get_group_permissions(self, user_group):
        return [self.permissions[u_g] for u_g in user_group if u_g in self.permissions.keys()]

    def test_permissions(self, user_permissions, uri_template, request_method):

        wala = user_permissions



        # get role attempt from uri
        # if uri_admin and

        # consolidate denny (gather all denny fields)
        # test denny against uri_template
        # if denny raise forbiden

        # consolidate allow
        # test allow against uri_template
        # if not allow raise forbiden

        # crazy regex to check uri vs permissions
        return None