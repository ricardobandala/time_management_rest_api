from falcon_auth import FalconAuthMiddleware, BasicAuthBackend


class Auth:

    def user_loader(username, password):
        return {'username': username}

    auth_backend = BasicAuthBackend(user_loader)
    auth = FalconAuthMiddleware(auth_backend, exempt_routes=['/login'], exempt_methods=['HEAD'])
