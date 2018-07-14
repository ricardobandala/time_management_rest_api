from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class TimeBlockNote(Base):
    __tablename__ = 'time_block_note'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    content = Column(String(1024), nullable=True)

    time_block_id = Column(Integer, ForeignKey('time_block.id'))
    time_block = relationship('TimeBlock', back_populates='time_block_note')

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
