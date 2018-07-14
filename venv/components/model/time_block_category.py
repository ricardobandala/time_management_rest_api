from sqlalchemy import Boolean, Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class TimeBlockCategory(Base):
    __tablename__ = 'time_block_category'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(512))

    # TODO define many to many association
    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
