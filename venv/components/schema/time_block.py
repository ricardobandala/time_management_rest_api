from sqlalchemy import Boolean, Column, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import DeclarativeBase


class Stint(DeclarativeBase):
    __tablename__ = 'stint'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    start_time = Column(DateTime, default=func.now(), nullable=False)
    stop_time = Column(DateTime, nullable=True)
    interruptions = Column(Integer, default=0)
    failed = Column(Boolean)

    stint_note = relationship('StintNoteModel', back_populates='stint')

    workday_id = Column(Integer, ForeignKey('workday.id'))
    workday = relationship('WorkdayModel', back_populates='stint')

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', back_populates='stint')

    category_id = Column(Integer, ForeignKey('stint_category.id'))
    category = relationship('StintCategory')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
