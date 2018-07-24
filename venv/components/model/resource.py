from base import DeclarativeBase
from sqlalchemy.event import listen
from sqlalchemy import Boolean, Column, DateTime, Integer, func, Enum, String, UniqueConstraint
import enum

from sqlalchemy.orm import relationship


class Action(enum.Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
    HEAD = 5
    PATCH = 6
    CONNECT = 7
    OPTIONS = 8
    TRACE = 9


class ResourceModel(DeclarativeBase):
    __tablename__ = 'resource'
    __table_args__ = (UniqueConstraint('route', 'action', name='uix_route_action'),)

    id = Column(Integer, primary_key=True, nullable=False)
    route = Column(String, nullable=False)
    action = Column(Enum(Action), nullable=False)
    is_active = Column(Boolean, default=False)
    exp_date = Column(DateTime)
    user = relationship('UserModel',
                                 secondary='user_resource',
                                 back_populates='user_resource',
                                 lazy="joined",
                                 uselist=True)



    # TODO IMPLEMENT ONE TO MANY
    # user_permission_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # user_permission = relationship('UserPermissionModel', back_populates='resource', lazy="joined")

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)