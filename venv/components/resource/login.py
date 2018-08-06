import json


class LoginItem:

    def on_post(self, req, resp):

        if 'user_token' in req.context:
            resp.body = json.dumps({
                'token': req.context['user_token'].decode('utf-8')
            })
