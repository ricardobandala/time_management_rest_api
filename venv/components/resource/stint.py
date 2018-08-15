import json
import falcon
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import raiseload
from sqlalchemy.orm.exc import NoResultFound
from model.identity import IdentityModel, IdentitySchema
from marshmallow import ValidationError


class Item:

    def on_get(self, req, resp, user_id):

        # Defining object shape and actions according to the role/ownership
        if req.context['user_role'] == 'admin':
            schema = IdentitySchema()
        elif req.context['user_id'] == user_id:
            schema = IdentitySchema(exclude=['id', 'user_id', 'created', 'modified', 'deleted'])
        else:
            raise falcon.HTTPForbidden()

        # fetching the object
        try:
            query = req.context['session'].query(IdentityModel).options(raiseload('*'))

            identity = query.filter(
                IdentityModel.user_id == user_id
            ).one()

            resp.body = schema.dumps(identity)

        except NoResultFound:
            raise falcon.HTTPNotFound()

    def on_post(self, req, resp):

        # Test for client errors
        try:
            identity = IdentitySchema().load(json.loads(req.stream.read()))
        except ValidationError as err:
            resp.body = err.messages['_schema']
            raise falcon.HTTP_BAD_REQUEST

        # Make data persistent
        try:
            req.context['session'].add(identity)
            req.context['session'].flush()
            resp.append_header('Content-Location', '{:s}/api/user/{:d}'.format(req.prefix, identity.id))
        except SQLAlchemyError:
            raise falcon.HTTPInternalServerError
        finally:
            req.context['session'].commit()

        # Response
        resp.status = falcon.HTTP_CREATED

    def on_put(self, req, resp, user_id):

        # Defining object shape and actions according to the role/ownership
        if req.context['user_role'] == 'admin':
            schema = IdentitySchema()
        elif req.context['user_id'] == user_id:
            schema = IdentitySchema(exclude=['id', 'user_id', 'created', 'modified', 'deleted'])
        else:
            raise falcon.HTTPForbidden()

        # Test for client errors
        try:
            identity = IdentitySchema().load(json.loads(req.stream.read()))
        except ValidationError as err:
            resp.body = err.messages['_schema']
            raise falcon.HTTP_BAD_REQUEST

        # Make data persistent
        try:
            req.context['session'].add(identity)
            req.context['session'].flush()
        except SQLAlchemyError:
            raise falcon.HTTPInternalServerError
        finally:
            req.context['session'].commit()

        # Response
        resp.status = falcon.HTTP_CREATED
        resp.append_header('Content-Location', '{:s}/api/user/{:d}'.format(req.prefix, identity.id))


class Collection:
    pass
