from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import DeclarativeBase


class TimeframeNoteModel(DeclarativeBase):
    __tablename__ = 'timeframe_note'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    content = Column(String(1024), nullable=True)

    timeframe_id = Column(Integer, ForeignKey('timeframe.id'))
    timeframe = relationship('TimeframeModel', back_populates='note')

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        TimeframeNoteModel(
            id={:d},  
            content={}, 
            timeframe={},
            user_id={:d},
            created={}, 
            modified={}, 
            deleted={} 
        )>""".format(
            self.id,
            self.content,
            self.timeframe,
            self.user_id,
            self.created,
            self.modified,
            self.deleted
        )
