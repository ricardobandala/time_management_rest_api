from datetime import timedelta
from sqlalchemy import Boolean, Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import DeclarativeBase


class Workday(DeclarativeBase):
    __tablename__ = 'workday'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, default=func.now(), nullable=False)
    # TODO, how to do dateadd in SQLite
    stop_time = Column(DateTime)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='workday')

    timeframe = relationship('Timeframe', back_populates='workday')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
