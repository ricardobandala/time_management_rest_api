from marshmallow import Schema, fields


class UserSchema(Schema):

    id = fields.Integer()
    username = fields.String()
    password = fields.String()
    is_active = fields.Boolean()

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime(dump_only=True)
