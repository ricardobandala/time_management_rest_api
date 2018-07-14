from sqlalchemy import Boolean, Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class UserProfile(Base):
    __tablename__ = 'user_profile'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='user_profile')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
