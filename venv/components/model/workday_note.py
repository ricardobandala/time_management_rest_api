from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from base import DeclarativeBase


class WorkdayNoteModel(DeclarativeBase):
    __tablename__ = 'workday_note'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    content = Column(String(1024), nullable=True)

    # MANY TO ONE
    workday_id = Column(Integer, ForeignKey('workday.id'))
    workday = relationship('WorkdayModel', back_populates='note', uselist=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', back_populates='workday_note', uselist=False)

    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, onupdate=func.now())
    deleted = Column(DateTime)

    def __repr__(self):
        return """<
        WorkdayNoteModel(
            id={:d},  
            content={}, 
            workday_id={:d},
            user_id={:d},
            created={}, 
            modified={}, 
            deleted={} 
        )>""".format(
            self.id,
            self.content,
            self.workday_id,
            self.user_id,
            self.created,
            self.modified,
            self.deleted
        )

