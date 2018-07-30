from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import fields, post_load, Schema
from base import DeclarativeBase


class StintNoteModel(DeclarativeBase):
    __tablename__ = 'stint_note'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    content = Column(String(1024), nullable=True)
    # TODO FIX, to MANY TO ONE
    # ONE TO MANY
    stint_id = Column(Integer, ForeignKey('stint.id'))
    stint = relationship('StintModel', back_populates='note', lazy='noload', uselist=False)
    # MANY TO ONE
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', lazy='noload', uselist=False)

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        StintNoteModel(
            id={:d},  
            content={}, 
            stint={},
            user_id={:d},
            created={}, 
            modified={}, 
            deleted={} 
        )>""".format(
            self.id,
            self.content,
            self.stint,
            self.user_id,
            self.created,
            self.modified,
            self.deleted
        )


class StintNoteSchema(Schema):

    id = fields.Integer(dump_only=True)
    content = fields.String()
    # MANY TO ONE
    stint_id = fields.Integer()
    stint = fields.Nested('StintSchema', many=False)
    user_id = fields.Integer()
    user = fields.Nested('UserSchema', many=False)

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime()

    @post_load
    def create_model(self, _model, data):
        return StintNoteModel(**data)