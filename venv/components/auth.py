import base64
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend
from model.user_login import UserLoginModel
from db import Database

session = Database().Session()


def handle_session(f):

    def wrapper(*args, **kwargs):
        try:
            user = f(*args, **kwargs)
        finally:
            session.close()
        return user
    return wrapper


@handle_session
def user_loader(username, password):
    user = session.query(UserLoginModel).filter(
        UserLoginModel.username == username,
        UserLoginModel.password == base64.b64encode(password.encode('utf-8'))
    ).one_or_none()

    return user


auth_backend = BasicAuthBackend(user_loader)


auth = FalconAuthMiddleware(
    auth_backend,
    exempt_routes=['/login'],
    exempt_methods=['HEAD']
)
