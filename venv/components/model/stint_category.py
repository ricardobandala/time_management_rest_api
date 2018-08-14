from base import DeclarativeBase
from marshmallow import fields, post_load, Schema
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship


class StintCategoryModel(DeclarativeBase):
    __tablename__ = 'stint_category'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(1024), unique=True)

    # MANY TO MANY
    stint = relationship(
        'StintModel',
        secondary='assoc_stint_stint_category',
        back_populates='category',
        lazy="noload",
        uselist=True
    )

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        StintCategoryModel(
            id={:d}, 
            name={} 
        )>""".format(
            self.id,
            self.name
        )


class StintCategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    description = fields.String()
    # MANY TO MANY
    stint = fields.Nested('StintSchema', many=True)

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime()

    @post_load
    def create_model(self, data):
        return StintCategoryModel(**data)
