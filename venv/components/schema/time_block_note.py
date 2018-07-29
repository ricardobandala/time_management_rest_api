from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import DeclarativeBase


class StintNoteModel(DeclarativeBase):
    __tablename__ = 'stint_note'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    content = Column(String(1024), nullable=True)

    stint_id = Column(Integer, ForeignKey('stint.id'))
    stint = relationship('Stint', back_populates='stint_note')

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)
