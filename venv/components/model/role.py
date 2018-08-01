from base import DeclarativeBase
import enum
from marshmallow import fields, post_load, Schema
from sqlalchemy import Boolean, Column, DateTime, Enum, func, Integer
from sqlalchemy.orm import relationship

from model.assoc_user_role import table as assoc_user_role_table


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

    # MANY TO ONE
    user = relationship(
        'UserModel',
        back_populates='role',
        secondary=assoc_user_role_table,
        lazy='noload'
    )

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """< RoleModel(
            id={self.id},
            title={self.title}, 
            is_active={self.is_active},
            created={self.created}, 
            modified={self.modified}, 
            deleted={self.deleted})>
            """.format(self=self).strip('\n')


class RoleSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    is_active = fields.Boolean()
    # MANY TO ONE
    user = fields.Nested('UserSchema', many=True)

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime()

    @post_load
    def create_model(self, _model, data):
        return RoleModel(**data)
