from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import fields, Schema
from base import DeclarativeBase


class TimeframeNoteModel(DeclarativeBase):
    __tablename__ = 'timeframe_note'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    content = Column(String(1024), nullable=True)
    # TODO FIX, to MANY TO ONE
    # ONE TO MANY
    timeframe_id = Column(Integer, ForeignKey('timeframe.id'))
    timeframe = relationship('TimeframeModel', back_populates='note', lazy='noload', uselist=False)
    # MANY TO ONE
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', lazy='noload', uselist=False)

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        TimeframeNoteModel(
            id={:d},  
            content={}, 
            timeframe={},
            user_id={:d},
            created={}, 
            modified={}, 
            deleted={} 
        )>""".format(
            self.id,
            self.content,
            self.timeframe,
            self.user_id,
            self.created,
            self.modified,
            self.deleted
        )


class TimeframeNoteSchema(Schema):

    id = fields.Integer()
    content = fields.String()
    # MANY TO ONE
    timeframe_id = fields.Integer()
    timeframe = fields.Nested('TimeframeSchema', many=False)
    user_id = fields.Integer()
    user = fields.Nested('UserSchema', many=False)

    created = fields.DateTime()
    modified = fields.DateTime()
    deleted = fields.DateTime()
