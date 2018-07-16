import base64
from base import DeclarativeBase
from sqlalchemy.event import listen
from sqlalchemy import Boolean, Column, DateTime, Integer, func, ForeignKey, String
from sqlalchemy.orm import relationship


class ResourceModel(DeclarativeBase):
    __tablename__ = 'resource'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    route = Column(String, unique=True, nullable=False)
    exp_date = Column(DateTime, nullable=False)

    # TODO IMPLEMENT ONE TO MANY
    # user_permission_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # user_permission = relationship('UserPermissionModel', back_populates='resource', lazy="joined")

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)