from marshmallow import Schema, fields


class UserProfile(Schema):

    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    user_id = fields.Integer()
    user = relationship('User', back_populates='indentity')

    created = field.DateTime()
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
