from sqlalchemy import create_engine
from base import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from db import Database
from model import *

db = Database()


# Destroy tables, and then create them again
def recreate_schema():
    DeclarativeBase.metadata.drop_all(db.engine)
    DeclarativeBase.metadata.create_all(db.engine)


def update_squema():
    DeclarativeBase.metadata.create_all(db.engine)


recreate_schema()
