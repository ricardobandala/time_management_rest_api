import base64
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend
from falcon_policy import RoleBasedPolicy
from policy import policy_config
from model.credential import CredentialModel
from model.user import UserModel
from model.credential import CredentialModel
from db import Database

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
            user = session.query(CredentialModel).filter(
                CredentialModel.username == username,
                CredentialModel.password == base64.b64encode(password.encode('utf-8'))
            ).one_or_none()

            return user

        return FalconAuthMiddleware(
            BasicAuthBackend(user_loader),
            self.exempt_routes,
            self.exempt_methods
        )


class Authorization(object):

    class RequestObject(object):
        def __init__(self, route: str, roles: str):
            self.route = route
            self.roles_header = roles
            self.provided_roles = [role.strip() for role in self.roles_header.split(',')]

    def process_request(self, req, resp):

        roles = req.context['session'].query(UserModel.role).filter(
            UserModel.id == req.context['user'].id
        ).one_or_none()

        RoleBasedPolicy(policy_config).process_resource(self.RequestObject(req.context.url, roles))

