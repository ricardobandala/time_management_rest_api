from sqlalchemy import create_engine
from base import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from db import Database
from model import UserModel, UserLoginModel, UserProfileModel
import base64

session = Database().Session()

###################################################
# Why this didn't work?

# user = UserModel(
#     username='awesome',
#     password='selfdestructive',
#     is_active=0
# )
# user_profile = UserProfileModel(
#     first_name='Peter',
#     last_name='Funk'
# )
# workday = WorkdayModel()
# time_block = TimeBlockModel()
# time_block_note = TimeBlockNoteModel()

# time_block.time_block_note = [time_block_note]
# workday.time_block = [time_block]
# user.workday = [workday]
# user.user_profile = [user_profile]
# session.add(user)
######################################################

# user = UserModel(
#     username='billy',
#     password='ihatemac',
#     is_active=1
# )
# user_profile = UserProfileModel(
#     first_name='Bill',
#     last_name='Gates'
# )
# workday = WorkdayModel()
# time_block = TimeBlockModel()
# time_block_note = TimeBlockNoteModel()
#
# user.time_block = [time_block]
# user.time_block_note = [time_block_note]
# user.workday = [workday]
# user.user_profile = [user_profile]
#
# time_block.time_block_note = [time_block_note]
# workday.time_block = [time_block]
#
# session.add(user)
########################################################################
# user = session.query(UserModel)\
#     .filter(UserModel.id == 7)\
#
# user = user.all()
# wala = user
######################################################################
# user = UserModel(
#     username='sdfsjbjbjbdfsdfs',
#     password='asfdfnbnbsd',
#     is_active=1
# )
# user_profile = UserProfileModel(
#     first_name='Scott',
#     last_name='Pilgrim2'
# )
# workday = WorkdayModel()
# user.workday = [workday]
# user.user_profile = [user_profile]
# session.add(user)
# session.commit()

######################################################################
#user = UserModel(
#    is_active=True
#)
#user.user_login = UserLoginModel(
#    username='ricardobandala',
#    password='123456789',
#    is_active=1,
#)
#user.user_profile = UserProfileModel(
#    first_name='Ricardo',
#    last_name='Bandala',
#    email='ricardobandala@pagefolio.com'
#)
#session.add(user)
#session.commit()

# session = {'query':5}
# u = 1


from functools import wraps


def handle_session(f):
    def wrapper(*args, **kwargs):
        try:
            user = f(*args, **kwargs)
        finally:
            session.close()
        return user
    return wrapper


@handle_session
def use_loader(username, password):
    user = session.query(UserLoginModel).filter(
        UserLoginModel.username == username,
        UserLoginModel.password == base64.b64encode(password.encode('utf-8'))
    ).one_or_none()

    return user


yora = use_loader(username='ricardobandala', password='123456789')
print(yora)