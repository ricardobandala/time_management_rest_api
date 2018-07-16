from sqlalchemy import create_engine
from base import Base
from sqlalchemy.orm import sessionmaker
from model import *

engine = create_engine('sqlite:///time_management.db')

Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)
