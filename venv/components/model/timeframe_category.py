from sqlalchemy import Boolean, Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
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
        lazy="joined",
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
