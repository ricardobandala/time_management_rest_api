from base import DeclarativeBase
from sqlalchemy import Column, Integer,  ForeignKey, Table


# Association table
table = Table(
    'assoc_stint_stint_category',
    DeclarativeBase.metadata,
    Column('stint_id', Integer, ForeignKey('stint.id')),
    Column('stint_category_id', Integer, ForeignKey('stint_category.id'))
)
