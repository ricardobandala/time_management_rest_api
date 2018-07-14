from sqlalchemy import create_engine
from base import Base
from sqlalchemy.orm import sessionmaker
from model.user import User

engine = create_engine('sqlite:///time_management.db')

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
