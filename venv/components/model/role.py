from base import DeclarativeBase
from sqlalchemy import Boolean, Column, DateTime, Enum, func, Integer
from sqlalchemy.orm import relationship
import enum


class RoleName(enum.Enum):
    admin = 1
    reporter = 2
    observer = 3


class RoleModel(DeclarativeBase):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Enum(RoleName), unique=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    user = relationship(
        'UserModel',
        secondary='assoc_user_role',
        back_populates='role',
        lazy="joined",
        uselist=True
    )

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
