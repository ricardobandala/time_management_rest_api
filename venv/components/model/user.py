import base64
from base import DeclarativeBase
from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship
from marshmallow import fields, Schema

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
    credential = relationship('CredentialModel', back_populates='user', lazy="joined", uselist=False)
    identity = relationship('IdentityModel', back_populates='user', lazy="joined", uselist=False)

    # ONE TO MANY
    workday = relationship('WorkdayModel', back_populates='user', uselist=True)
    workday_note = relationship('WorkdayNoteModel', back_populates='user', uselist=True)

    timeframe = relationship('TimeframeModel', back_populates='user', uselist=True)
    timeframe_note = relationship('TimeframeNoteModel', back_populates='user', uselist=True)

    # MANY TO ONE
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship('RoleModel', back_populates='user', uselist=False)

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def get_role(self):
        return self.role.title.name

    def __repr__(self):
        return """" <UserModel(
                id={:d}, 
                is_active={}, 
                start_date={},
                end_date={},
                created={}, modified={}, deleted={})>)""".format(
            self.id,
            self.is_active,
            self.start_date,
            self.end_date,
            self.created,
            self.modified,
            self.deleted
        )


class UserSchema(Schema):

    id = fields.Integer()
    is_active = fields.Boolean()
    start_date = fields.DateTime()
    end_date = fields.DateTime()

    # credential = relationship("CredentialModel', back_populates='user', lazy="joined", uselist=False)
    # identity = relationship('IdentityModel', back_populates='user', lazy="joined", uselist=False)
    # workday = relationship('WorkdayModel', back_populates='user')
    # timeframe = relationship('Timeframe', back_populates='user')

    created = fields.DateTime()
    modified = fields.DateTime()
    deleted = fields.DateTime()
