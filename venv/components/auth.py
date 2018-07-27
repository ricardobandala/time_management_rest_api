import base64
import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend
from falcon_policy import RoleBasedPolicy
from policy import policy_config
from model.user import UserModel
from model.role import RoleModel
from model.credential import CredentialModel
from db import Database
from sqlalchemy.orm import contains_eager

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
            ).one()

            return credential

        return FalconAuthMiddleware(
            BasicAuthBackend(user_loader),
            self.exempt_routes,
            self.exempt_methods
        )


class Authorization(object):

    def process_resource(self, req, resp, resource, params):

        user = req.context['session'].query(UserModel).filter(
            UserModel.id == req.context['user'].user_id
        ).one_or_none()

        # TODO, how can I modify the header
        # req.headers.update({'X-ROLES': getattr(user.role.name, 'name', '')})

        if not req.get_header('X-Roles', default='') == user.get_role():
            raise falcon.HTTPForbidden(
                description='Access to this resource has been restricted'
            )

        RoleBasedPolicy(policy_config).process_resource(
            req,
            resp,
            resource,
            params
        )

