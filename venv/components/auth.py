import base64
import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend
from falcon_policy import RoleBasedPolicy
from sqlalchemy.orm import joinedload, raiseload
from policy.config import policy_definition
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

    def process_resource(self, req, resp, resource, params):

        query = req.context['session'].query(UserModel)\
            .options(joinedload(UserModel.role), raiseload('*'))

        user = query.filter(
            UserModel.id == req.context['user'].user_id
        ).one_or_none()

        # TODO, how can I modify the header
        # req.headers.update({'X-ROLES': getattr(user.role.name, 'name', '')})

        if not user.get_role() == req.get_header('X-Roles', default=''):
            raise falcon.HTTPForbidden(
                description='Access to this resource has been restricted'
            )
        else:
            req.context['user_role'] = user.get_role()

        RoleBasedPolicy(policy_definition).process_resource(req, resp, resource, params)

