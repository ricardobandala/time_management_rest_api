from base import DeclarativeBase
from sqlalchemy import Boolean, Column, DateTime, Enum, func, Integer
from sqlalchemy.orm import relationship
import enum


class RoleName(enum.Enum):
    admin = 'admin'
    reporter = 'reporter'
    observer = 'observer'

# TODO, check why this is not working, implementation as described in the docs
def enum_values(enum_class):
    return [e.value for e in enum_class]


class RoleModel(DeclarativeBase):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(Enum(RoleName, values_callable=enum_values), unique=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    user = relationship('UserModel', back_populates='role')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return (
            "< RoleModel("
            "id={:d}, name={}, is_active={}, "
            "created={}, modified={}, deleted={})>"
        ).format(
            self.id,
            self.name,
            self.is_active,
            self.created,
            self.modified,
            self.deleted
        )