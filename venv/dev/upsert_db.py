from sqlalchemy import create_engine
from base import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from db import Database
from model import UserModel, UserProfileModel, UserLoginModel

engine = create_engine(Database.URL)

Session = sessionmaker()
Session.configure(bind=engine)
DeclarativeBase.metadata.create_all(engine)
