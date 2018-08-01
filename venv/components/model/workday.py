from base import DeclarativeBase
from marshmallow import fields, post_load, Schema
from sqlalchemy import Column, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import relationship


class WorkdayModel(DeclarativeBase):
    __tablename__ = 'workday'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, default=func.now(), nullable=False)
    # TODO, how to do dateadd in SQLite
    stop_time = Column(DateTime)

    # ONE TO MANY
    stint = relationship('StintModel', back_populates='workday', lazy='noload', uselist=True)
    note = relationship('WorkdayNoteModel', back_populates='workday', lazy='noload', uselist=True)

    # MANY TO ONE
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    user = relationship('UserModel', back_populates='workday', lazy='noload', uselist=False)

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        WorkdayModel(
            id={:d},  
            start_time={}, 
            stop_time={},
            stint={},
            user_id={:d}, 
            created={} 
            modified={} 
            deleted={} 
        )>""".format(
            self.id,
            self.start_time,
            self.stop_time,
            self.stint,
            self.user_id,
            self.created,
            self.modified,
            self.deleted
        )


class WorkdaySchema(Schema):
    id = fields.Integer(dump_only=True)
    start_time = fields.DateTime()
    stop_time = fields.DateTime()
    # ONE TO MANY
    stint = fields.Nested('StintSchema', many=True)
    note = fields.Nested('WorkdayNoteSchema', many=True)
    # MANY TO ONE
    user_id = fields.Integer()
    user = fields.Nested('UserSchema', many=False)

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime()

    @post_load
    def create_model(self, _model, data):
        return WorkdayModel(**data)

