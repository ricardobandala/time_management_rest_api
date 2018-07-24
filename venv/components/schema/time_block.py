from sqlalchemy import Boolean, Column, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import DeclarativeBase


class Timeframe(DeclarativeBase):
    __tablename__ = 'timeframe'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    start_time = Column(DateTime, default=func.now(), nullable=False)
    stop_time = Column(DateTime, nullable=True)
    interruptions = Column(Integer, default=0)
    failed = Column(Boolean)

    timeframe_note = relationship('TimeframeNoteModel', back_populates='timeframe')

    workday_id = Column(Integer, ForeignKey('workday.id'))
    workday = relationship('Workday', back_populates='timeframe')

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='timeframe')

    category_id = Column(Integer, ForeignKey('timeframe_category.id'))
    category = relationship('TimeframeCategory')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
