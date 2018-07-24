from db import Database
from model import *

session = Database().Session()

session.add_all([

    # TODO Solve semantic problem POST no parameter for item or collection

    # USER ###############################################
    # Item
    ResourceModel(route='/user/', action='POST', is_active=True),
    ResourceModel(route='/user/{user_id:int}', action='GET', is_active=True),
    ResourceModel(route='/user/{user_id:int}', action='PUT', is_active=True),
    ResourceModel(route='/user/{user_id:int}', action='DELETE', is_active=True),
    # Collection

    # ResourceModel(route='/user/', action='POST', is_active=True),
    ResourceModel(route='/user/', action='GET', is_active=True),
    ResourceModel(route='/user/', action='PUT', is_active=True),
    ResourceModel(route='/user/', action='DELETE', is_active=True),
    # Abstract


    # USER LOGIN ###############################################
    # Item
    ResourceModel(route='/user_login/', action='POST', is_active=True),
    ResourceModel(route='/user_login/{user_login_id:int}', action='GET', is_active=True),
    ResourceModel(route='/user_login/{user_login_id:int}', action='PUT', is_active=True),
    ResourceModel(route='/user_login/{user_login_id:int}', action='DELETE', is_active=True),
    # Collection

    # ResourceModel(route='/user_login/', action='POST', is_active=True),
    ResourceModel(route='/user_login/', action='GET', is_active=True),
    ResourceModel(route='/user_login/', action='PUT', is_active=True),
    ResourceModel(route='/user_login/', action='DELETE', is_active=True),
    # Abstract

    # USER PROFILE ###############################################
    # Item
    ResourceModel(route='/user_profile/', action='POST', is_active=True),
    ResourceModel(route='/user_profile/{user_profile_id:int}', action='GET', is_active=True),
    ResourceModel(route='/user_profile/{user_profile_id:int}', action='PUT', is_active=True),
    ResourceModel(route='/user_profile/{user_profile_id:int}', action='DELETE', is_active=True),
    # Collection

    # ResourceModel(route='/user_profile/', action='POST', is_active=True),
    ResourceModel(route='/user_profile/', action='GET', is_active=True),
    ResourceModel(route='/user_profile/', action='PUT', is_active=True),
    ResourceModel(route='/user_profile/', action='DELETE', is_active=True),
    # Abstract


    # WORKDAY ###############################################
    # Item
    ResourceModel(route='/workday/', action='POST', is_active=True),
    ResourceModel(route='/workday/{workday_id:int}', action='GET', is_active=True),
    ResourceModel(route='/workday/{workday_id:int}', action='PUT', is_active=True),
    ResourceModel(route='/workday/{workday_id:int}', action='DELETE', is_active=True),
    # Collection
    # ResourceModel(route='/workday/', action='POST', is_active=True),
    ResourceModel(route='/workday/', action='GET', is_active=True),
    ResourceModel(route='/workday/', action='PUT', is_active=True),
    ResourceModel(route='/workday/', action='DELETE', is_active=True),
    # Abstract

    # TIME BLOCK ###############################################
    ResourceModel(route='/time_block/', action='POST', is_active=True),
    ResourceModel(route='/time_block/{time_block_id:int}', action='GET', is_active=True),
    ResourceModel(route='/time_block/{time_block_id:int}', action='PUT', is_active=True),
    ResourceModel(route='/time_block/{time_block_id:int}', action='DELETE', is_active=True),

    # ResourceModel(route='/time_block/', action='POST', is_active=True),
    ResourceModel(route='/time_block/', action='GET', is_active=True),
    ResourceModel(route='/time_block/', action='PUT', is_active=True),
    ResourceModel(route='/time_block/', action='DELETE', is_active=True),
    # Abstract

    # TIME BLOCK NOTE ###############################################
    ResourceModel(route='/time_block_note/', action='POST', is_active=True),
    ResourceModel(route='/time_block_note/{time_block_note_id:int}', action='GET', is_active=True),
    ResourceModel(route='/time_block_note/{time_block_note_id:int}', action='PUT', is_active=True),
    ResourceModel(route='/time_block_note/{time_block_note_id:int}', action='DELETE', is_active=True),

    # ResourceModel(route='/time_block_note/', action='POST', is_active=True),
    ResourceModel(route='/time_block_note/', action='GET', is_active=True),
    ResourceModel(route='/time_block_note/', action='PUT', is_active=True),
    ResourceModel(route='/time_block_note/', action='DELETE', is_active=True),
    # Abstract

    # TIME BLOCK CATEGORY ###############################################
    ResourceModel(route='/time_block_category/', action='POST', is_active=True),
    ResourceModel(route='/time_block_category/{time_block_category_id:int}', action='GET', is_active=True),
    ResourceModel(route='/time_block_category/{time_block_category_id:int}', action='PUT', is_active=True),
    ResourceModel(route='/time_block_category/{time_block_category_id:int}', action='DELETE', is_active=True),

    # ResourceModel(route='/time_block_category/', action='POST', is_active=True),
    ResourceModel(route='/time_block_category/', action='GET', is_active=True),
    ResourceModel(route='/time_block_category/', action='PUT', is_active=True),
    ResourceModel(route='/time_block_category/', action='DELETE', is_active=True)
    # Abstract
])

session.commit()


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


