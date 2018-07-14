from datetime import timedelta
from sqlalchemy import Boolean, Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Workday(Base):
    __tablename__ = 'workday'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, default=func.now(), nullable=False)
    stop_time = Column(DateTime, default=func.now() + timedelta(hours=8))

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='workday')

    time_block = relationship('TimeBlock', back_populates='workday')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
