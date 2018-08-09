import json
import falcon
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import raiseload
from sqlalchemy.orm.exc import NoResultFound
from model.user import UserModel, UserSchema
from marshmallow import ValidationError


class Item:

    def on_get(self, req, resp, user_id):
        try:
            query = req.context['session'].query(UserModel).options(raiseload('*'))
            user = query.filter(UserModel.id == user_id).one()
        except NoResultFound:
            raise falcon.HTTPNotFound()

        resp.body = UserSchema(only=['id', 'is_active', 'start_date', 'end_date', 'role_id']).dumps(user)

    def on_post(self, req, resp):

        # Test for client errors
        try:
            user = UserSchema().load(json.loads(req.stream.read()))
        except ValidationError as err:
            resp.body = err.messages['_schema']
            raise falcon.HTTP_BAD_REQUEST

        # Make data persistent
        try:
            req.context['session'].add(user)
            req.context['session'].flush()
        except SQLAlchemyError:
            raise falcon.HTTPInternalServerError
        finally:
            req.context['session'].commit()

        # Response
        resp.status = falcon.HTTP_CREATED
        resp.append_header('Content-Location', '{:s}/api/user/{:d}'.format(req.prefix, user.id))

    def on_put(self, req, resp, user_id):
        pass


class Collection:
    pass
