import base64
from sqlalchemy.event import listen
from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, func, String
from sqlalchemy.orm import relationship
from marshmallow import fields, Schema
from base import DeclarativeBase


class CredentialModel(DeclarativeBase):
    __tablename__ = 'credential'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=0)

    # ONE TO ONE
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('UserModel', back_populates='credential', lazy="noload")

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        CredentialModel(
            id={:d}, 
            username={}, 
            is_active={:d}, 
            created={}, 
            modified={}, 
            deleted={} 
        )>""".format(
            self.id,
            self.username,
            self.is_active,
            self.created,
            self.modified,
            self.deleted
        )


listen(
    CredentialModel.password,
    'set',
    lambda target, value, oldvalue, initiator: base64.b64encode(value.encode('utf-8')),
    # TODO verify if this logic to check if is encoded before encode
    # base64.b64encode(value.encode('utf-8')) if base64.b64encode(base64.b64decode(value)) != value else value
    retval=True
)


class CredentialSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    password = fields.String()
    is_active = fields.Boolean()

    # ONE TO ONE
    user_id = fields.Integer()
    user = fields.Nested('UserSchema', many=False)

    created = fields.DateTime()
    modified = fields.DateTime()
    deleted = fields.DateTime()
