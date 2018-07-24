from sqlalchemy import create_engine
from base import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from db import Database
from model import *

db = Database()
DeclarativeBase.metadata.create_all(db.engine)
