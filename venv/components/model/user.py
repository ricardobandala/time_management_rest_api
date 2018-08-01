from base import DeclarativeBase
from marshmallow import fields, post_load, Schema
from model.assoc_user_role import table as assoc_user_role_table
from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship

"""
User is actually a UserApplication, but we tried to avoid verbosity
"""


class UserModel(DeclarativeBase):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    # ONE TO ONE
    # TODO, credential_id and identity_id, dont forget to update Schema and Resource
    credential = relationship('CredentialModel', back_populates='user', lazy="noload", uselist=False)
    identity = relationship('IdentityModel', back_populates='user', lazy="noload", uselist=False)

    # ONE TO MANY
    workday = relationship('WorkdayModel', back_populates='user', uselist=True, lazy='noload')
    workday_note = relationship('WorkdayNoteModel', back_populates='user', uselist=True)

    stint = relationship('StintModel', back_populates='user', lazy="noload", uselist=True, )
    stint_note = relationship('StintNoteModel', back_populates='user', lazy="noload", uselist=True)

    # MANY TO MANY
    role = relationship(
        'RoleModel',
        back_populates='user',
        secondary=assoc_user_role_table,
        lazy="noload"
    )

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def get_role(self):
        # TODO, Am I obscuring through this getter?
        return self.role.title.name

    def __repr__(self):
        return """" <UserModel(
                id={self.id}, 
                is_active={self.is_active},
                role={self.role}, 
                start_date={self.start_date},
                end_date={self.end_date},
                created={self.created}, 
                modified={self.modified}, 
                deleted={self.delete})>)
                """.format(self=self).strip('\n')


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    is_active = fields.Boolean()
    start_date = fields.DateTime()
    end_date = fields.DateTime()
    # Single Nest
    credential = fields.Nested('CredentialSchema')
    identity = fields.Nested('IdentitySchema')
    role_id = fields.Integer()
    role = fields.Nested('RoleSchema')
    # Many Nest
    workday = fields.Nested('WorkdaySchema', many=True)
    workday_note = fields.Nested('WorkdayNoteSchema', many=True)
    stint = fields.Nested('StintSchema', many=True)
    stint_note = fields.Nested('StintNoteSchema', many=True)

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime()

    @post_load
    def create_model(self, data):
        return UserModel(**data)
