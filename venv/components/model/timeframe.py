from sqlalchemy import Boolean, Column, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import DeclarativeBase


class TimeframeModel(DeclarativeBase):
    __tablename__ = 'timeframe'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)

    start_time = Column(DateTime, default=func.now(), nullable=False)
    stop_time = Column(DateTime, nullable=True)
    interruptions = Column(Integer, default=0)
    failed = Column(Boolean)

    # ONE TO MANY
    note = relationship('TimeframeNoteModel', back_populates='timeframe', uselist=True)

    # MANY TO ONE
    workday_id = Column(Integer, ForeignKey('workday.id'))
    workday = relationship('WorkdayModel', back_populates='timeframe')

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', back_populates='timeframe')

    # MANY TO MANY
    category = relationship(
        'TimeframeCategoryModel',
        secondary='assoc_timeframe_timeframe_category',
        back_populates='timeframe',
        lazy="joined",
        uselist=True
    )

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        TimeframeModel(
            id={:d}, 
            start_time={}, 
            stop_time={}, 
            interruptions={:d},
            failed={},
            created={}, 
            modified={}, 
            deleted={} 
        )>""".format(
            self.id,
            self.start_time,
            self.stop_time,
            self.interruptions,
            self.failed,
            self.created,
            self.modified,
            self.deleted
        )

