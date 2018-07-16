import base64
from sqlalchemy.event import listen
from sqlalchemy import Boolean, Column, DateTime, Integer,  ForeignKey, func, String
from sqlalchemy.orm import relationship
# from marshmallow import fields, Schema
from base import DeclarativeBase


class UserPermissionModel(DeclarativeBase):
    __tablename__ = 'user_permission'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    resource_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # TODO composed contraint key

    resource = relationship('ResourceModel', ForeignKey('resource.id'), nullable=False)

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return "<UserLogin(id={:d}, username={}, is_active={:d}, created={}, modified={}, deleted={} )>"\
               .format(
                   self.id,
                   self.username,
                   self.is_active,
                   self.created,
                   self.modified,
                   self.deleted
               )



listen(
    UserLoginModel.password,
    'set',
    lambda target, value, oldvalue, initiator: base64.b64encode(value.encode('utf-8')),
    # TODO verify if this logic to check if is encoded before encode
    # base64.b64encode(value.encode('utf-8')) if base64.b64encode(base64.b64decode(value)) != value else value
    retval=True
)




# class UserLoginSchema:
#
#     id = fields.Integer()
#     username = fields.String()
#     password = fields.String()
#     is_active = fields.Boolean()
#
#     created = fields.DateTime()
#     modified = fields.DateTime()
#     deleted = fields.DateTime()