import json
import falcon
from model.user import User as Model


class Item:

    def on_get(self, req, resp, user_id):
        resp.body = 'Oia'
        # query = req.context['session'].query(Model)
        # query = query.filter(Model.id == user_id)
        # user = query.one_or_none()
        #
        # if not user:
        #     raise falcon.HTTPNotFound()

        # resp.body = UserSchema(only=('username', 'is_active')).dumps(user)

    def on_post(self, req, resp):
        pass
        # data = UserSchema().load(json.loads(req.stream.read()))
        # req.context['session'].add(data)
        # req.context['session'].commit()

    def on_put(self, req, resp, user_id):
        pass
        # data = UserSchema().load(json.loads(req.stream.read())).data
        # req.context['session'].add(data)
        # req.context['session'].commit()


class Collection:
    pass
