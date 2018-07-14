from sqlalchemy import Boolean, Column, DateTime, String, Integer, func
from sqlalchemy.orm import relationship
from base import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean)
    user_profile = relationship('UserProfile', back_populates='user')
    workday = relationship('Workday', back_populates='user')
    time_block = relationship('TimeBlock', back_populates='user')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
