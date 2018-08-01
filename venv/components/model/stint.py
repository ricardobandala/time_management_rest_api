from base import DeclarativeBase
from marshmallow import fields, post_load, Schema
from model.assoc_stint_stint_category import table as assoc_stint_stint_category_table
from sqlalchemy import Boolean, Column, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import relationship



class StintModel(DeclarativeBase):
    """
     Just in case you're curious about what a stint is: http://www.learnersdictionary.com/definition/stint
    noun:
        a period of time spent doing a certain job or activity
    verb:
        to use or give something in limited amounts
    """
    __tablename__ = 'stint'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    start_time = Column(DateTime, default=func.now(), nullable=False)
    stop_time = Column(DateTime, nullable=True)
    interruptions = Column(Integer, default=0)
    failed = Column(Boolean)

    # ONE TO MANY
    note = relationship(
        'StintNoteModel',
        back_populates='stint',
        uselist=True,
        lazy='noload'
    )

    # MANY TO ONE
    workday_id = Column(Integer, ForeignKey('workday.id'), nullable=False, index=True)
    workday = relationship('WorkdayModel', back_populates='stint', uselist=False, lazy='noload')

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    user = relationship('UserModel', back_populates='stint', uselist=False, lazy='noload')

    # MANY TO MANY
    category = relationship(
        'StintCategoryModel',
        back_populates='stint',
        secondary=assoc_stint_stint_category_table,
        lazy="noload",
        uselist=True
    )

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        StintModel(
            id={:d}, 
            start_time={}, 
            stop_time={}, 
            interruptions={:d},
            failed={},
            created={}, 
            modified={}, 
            deleted={} 
        )>""".format(
            self.id,
            self.start_time,
            self.stop_time,
            self.interruptions,
            self.failed,
            self.created,
            self.modified,
            self.deleted
        )


class StintSchema(Schema):
    id = fields.Integer(dump_only=True)
    start_time = fields.DateTime()
    stop_time = fields.DateTime()
    interruptions = fields.Integer()
    failed = fields.Boolean()

    # ONE TO MANY
    note = fields.Nested('StintNoteSchema', many=True)
    # MANY TO ONE
    workday_id = fields.Integer()
    workday = fields.Nested('WorkdaySchema', many=False)
    user_id = fields.Integer()
    user = fields.Nested('UserSchema', many=False)
    # MANY TO MANY
    category = fields.Nested('StintCategorySchema', many=True)

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime()

    @post_load
    def create_model(self, _model, data):
        return StintModel(**data)
