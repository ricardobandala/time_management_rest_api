from sqlalchemy import Boolean, Column, DateTime, String, Integer, func, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from base import DeclarativeBase
from marshmallow import fields, post_load, Schema, validates


class IdentityModel(DeclarativeBase):
    __tablename__ = 'indentity'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255))
    # ONE TO ONE
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('UserModel', back_populates='identity', lazy="noload")

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        IdentityModel(
            id={:d}, 
            first_name={}, 
            last_name={}, 
            email={},
            user_id={},
            created={}, 
            modified={}, 
            deleted={} 
        )>""".format(
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.user_id,
            self.created,
            self.modified,
            self.deleted
        )


class IdentitySchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    # ONE TO ONE
    user_id = fields.Integer(required=True)
    user = fields.Nested('UserSchema', many=False)

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime()

    @post_load
    def create_model(self, _model, data):
        return IdentityModel(**data)

