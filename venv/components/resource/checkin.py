import datetime
import json
import falcon
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import raiseload
from sqlalchemy.orm.exc import NoResultFound
from model.user import UserModel, UserSchema
from model.workday import WorkdayModel, WorkdaySchema
from model.stint import StintModel, StintSchema
from marshmallow import ValidationError
from domain_logic import config
import pytz


class Item:

    def on_post(self, req, resp):

        try:
            start_time = datetime.datetime.now(tz=pytz.UTC)
            stop_time = start_time + datetime.timedelta(minutes=config['deltas']['workday_length'])
            user_id = req.context['user_permission']['sub']

            workday = WorkdaySchema().load({
                'start_time': start_time.isoformat(),
                'stop_time': stop_time.isoformat(),
                'user_id': user_id
            })
            # The first element starts at the same time than the workday
            next_start_time = start_time

            for item in config['templates']['workday']['classic']['structure']:

                if item is config['entities']['short_rest']:
                    next_start_time = next_start_time + datetime.timedelta(minutes=config['deltas']['short_rest_length'])

                elif item is config['entities']['long_rest']:
                    next_start_time = next_start_time + datetime.timedelta(minutes=config['deltas']['short_rest_length'])

                elif item is config['entities']['lunch']:
                    next_start_time = next_start_time + datetime.timedelta(minutes=config['deltas']['lunch_length'])

                if item is config['entities']['stint']:

                    next_stop_time = next_start_time + datetime.timedelta(minutes=config['deltas']['stint_length'])

                    workday.stint.append(StintSchema().load({
                        'start_time': next_start_time.isoformat(),
                        'stop_time': next_stop_time.isoformat(),
                        'user_id': user_id
                    }))

                    next_start_time = next_stop_time
                else:
                    pass  # TODO Throw error

        except ValidationError as err:
            resp.body = err.messages['_schema']
            raise falcon.HTTP_BAD_REQUEST

        # Make data persistent
        try:
            req.context['session'].add(workday)
            req.context['session'].flush()
        except SQLAlchemyError:
            raise falcon.HTTPInternalServerError
        finally:
            req.context['session'].commit()

        # Response
        resp.status = falcon.HTTP_CREATED
        resp.append_header('Content-Location', '{:s}/api/user/{:d}'.format(req.prefix, workday.id))
