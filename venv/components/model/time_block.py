from sqlalchemy import Boolean, Column, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class TimeBlock(Base):
    __tablename__ = 'time_block'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    start_time = Column(DateTime, default=func.now(), nullable=False)
    stop_time = Column(DateTime, nullable=True)
    interruptions = Column(Integer, default=0)
    failed = Column(Boolean)

    time_block_note = relationship('TimeBlockNote', back_populates='time_block')

    workday_id = Column(Integer, ForeignKey('workday.id'))
    workday = relationship('Workday', back_populates='time_block')

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='time_block')

    category_id = Column(Integer, ForeignKey('time_block_category.id'))
    category = relationship('TimeBlockCategory')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
