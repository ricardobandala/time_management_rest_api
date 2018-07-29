from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import fields, Schema
from base import DeclarativeBase


class TimeframeCategoryModel(DeclarativeBase):
    __tablename__ = 'timeframe_category'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(1024), unique=True)

    # MANY TO MANY
    timeframe = relationship(
        'TimeframeModel',
        secondary='assoc_timeframe_timeframe_category',
        back_populates='category',
        lazy="noload",
        uselist=True
    )

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        TimeframeCategoryModel(
            id={:d}, 
            name={} 
        )>""".format(
            self.id,
            self.name
        )


class TimeframeCategorySchema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    # MANY TO MANY
    timeframe = fields.Nested('TimeframeSchema', many=True)

    created = fields.DateTime()
    modified = fields.DateTime()
    deleted = fields.DateTime()
