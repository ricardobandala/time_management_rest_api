from base import DeclarativeBase
from sqlalchemy import Column, Integer,  ForeignKey, Table

table = association_table = Table(
    'assoc_user_role',
    DeclarativeBase.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('role.id'), primary_key=True)
)
