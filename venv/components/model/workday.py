from datetime import timedelta
from sqlalchemy import Boolean, Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import DeclarativeBase


class WorkdayModel(DeclarativeBase):
    __tablename__ = 'workday'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, default=func.now(), nullable=False)
    # TODO, how to do dateadd in SQLite
    stop_time = Column(DateTime)

    # ONE TO MANY
    timeframe = relationship('TimeframeModel', back_populates='workday', uselist=True)
    note = relationship('WorkdayNoteModel', back_populates='workday', uselist=True)

    # MANY TO ONE
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', back_populates='workday')

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        WorkdayModel(
            id={:d},  
            start_time={}, 
            stop_time={},
            timeframe={},
            user_id={:d}, 
            created={} 
            modified={} 
            deleted={} 
        )>""".format(
            self.id,
            self.start_time,
            self.stop_time,
            self.timeframe,
            self.user_id,
            self.created,
            self.modified,
            self.deleted
        )

