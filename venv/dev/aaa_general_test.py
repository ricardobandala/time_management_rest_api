from sqlalchemy import create_engine
from base import Base
from sqlalchemy.orm import sessionmaker
from model import *
import base64

engine = create_engine('sqlite:///time_management.db')

Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)

session = Session()

# user = UserModel(
#     username='ricardobandala',
#     password=base64.encode('secret'),
#     is_active=1
# )
# user.user_profile = [UserProfileModel(
#     first_name='ricardo',
#     last_name='bandala'
# )]

user = session.query(UserModel).filter(UserModel.id == 1).one_or_none()
user.password = base64.b64encode(user.password.encode('utf-8'))
session.commit()
