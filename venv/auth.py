import base64
import datetime
from db import Database
import falcon
from falcon_auth import BasicAuthBackend, JWTAuthBackend
import jwt
from model.user import UserModel
from model.credential import CredentialModel
import re
from sqlalchemy.orm import joinedload

session = Database().Session()


def _session_handler(f):
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        finally:
            session.close()
        return result

    return wrapper


class Authentication(object):

    def process_request(self, req, resp):
        auth = req.get_header('Authorization')
        if re.search(r'Basic', auth):
            user = BasicAuthBackend(self.get_user).authenticate(req, resp, None)
            req.context.update({'user': user})
            return
        elif re.search(r'Bearer', auth):
            pass
        else:
            raise falcon.HTTPBadRequest()

    @_session_handler
    def get_user(self, username: str, password: str):
        query = session.query(UserModel)
        query = query.join(UserModel.credential).join(UserModel.role)
        return query.filter(
            CredentialModel.username == username,
            CredentialModel.password == base64.b64encode(password.encode('utf-8'))
        ).options(joinedload(UserModel.role)).one()


class TokenHandler(object):
    def __init__(self, login_route:str, key:str, headers:dict, minutes_lifespan:int, permission_handler):
        self.login_route = login_route
        self.key = key
        self.headers = headers
        self.minutes_lifespan = minutes_lifespan
        self.permission_handler = permission_handler

    def process_resource(self, req, resp, resource, params):
        auth = req.get_header('Authorization')

        if re.search(r'Bearer', auth):
            jwt_method = JWTAuthBackend(
                user_loader=lambda x: x,
                secret_key=self.key,
                algorithm=self.headers['alg'],
                auth_header_prefix='Bearer',
                required_claims=['exp']
            )
            user_permission = jwt_method.authenticate(req, resp, resource)

            req.context.update({'user_permission': user_permission})

        elif re.search(r'Basic', auth) and req.uri_template == self.login_route:
            user_permissions = self.permission_handler.get_permissions(req.context['user'].get_role())
            if not user_permissions:
                falcon.HTTPForbidden()

            token = self.create({'sub': req.context['user'].id, 'permission': user_permissions})
            if not token:
                falcon.HTTPForbidden()
            req.context.update({'user_token': token})
        else:
            raise falcon.HTTPBadRequest()

    def get_encoded(self, payload: dict):
        return jwt.encode(payload, key=self.key, algorithm=self.headers['alg'], headers=self.headers)

    def get_decoded(self, payload: dict):
        return jwt.decode(payload, self.key, algorithms=['HS256'])

    def create(self, payload):
        # TODO implement TRY
        if 'exp' not in payload:
            now = datetime.datetime.utcnow()
            exp = (now+datetime.timedelta(minutes = self.minutes_lifespan)).timestamp()
            payload.update({
                'exp': exp
            })
        return self.get_encoded(payload)


class Permission:
    def __init__(self, roles, groups, permissions):
        self.roles = roles
        self.groups = groups
        self.permissions = permissions

    def get_permissions(self, role):
        group = self._get_role_group(role)
        permissions = self._get_group_permission(group)
        if not permissions:
            raise falcon.HTTPForbidden()
        return permissions

    def _get_role_group(self, user_role: list):
        intersection = list(set(user_role) & set(self.roles))
        if not intersection:
            falcon.HTTPForbidden()
        else:
            return [k for k, v in self.groups.items() if list(set(v) & set(intersection))]

    def _get_group_permission(self, user_group):
        return [self.permissions[u_g] for u_g in user_group if u_g in self.permissions.keys()]


class Authorization(object):
    def __init__(self, app_permissions: dict, exempt_routes: list):
        self.app_permissions = app_permissions
        self.exempt_routes = exempt_routes

    def process_resource(self, req, resp, resource, params):
        if req.uri_template not in self.exempt_routes:
            self.test_permissions(req.context['user_permission']['permission'], req.uri_template, req.method)

    def test_permissions(self, user_permissions, uri_template, request_method):

        # Get allow and deny from all the permissions in separate lists
        allow = dict()
        deny = dict()
        [
            allow.update(upv) if upk == 'allow'
            else deny.update(upv) if upk == 'deny'
            else None
            for up in user_permissions for upk, upv in up.items()
        ]

        """ 
        Star means all methods, therefore when present it has to be the only one in the array ['*'] "
        the first iteration is to test for explicit denial on route or method
        the second iteration is to test for explicit approval on route or method
        """
        if any([
            re.search(route, uri_template) and ('*' in methods or request_method in methods) for route, methods in
                deny.items()]):
            raise falcon.HTTPForbidden()

        if not any([
            re.search(route, uri_template) and ('*' in methods or request_method in methods) for route, methods in
                allow.items()]):
            raise falcon.HTTPForbidden()
