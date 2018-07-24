from sqlalchemy import Column, Integer,  ForeignKey
from base import DeclarativeBase


# Association table
class TimeframeTimeframeCategoryModel(DeclarativeBase):
    __tablename__ = 'assoc_timeframe_timeframe_category'
    __table_args__ = {'extend_existing': True}

    timeframe_id = Column(Integer, ForeignKey('timeframe.id'), primary_key=True)
    timeframe_category_id = Column(Integer, ForeignKey('timeframe_category.id'), primary_key=True)

    def __repr__(self):
        return """
        <TimeframeTimeframeCategoryModel(
            timeframe_id={:d}, 
            timeframe_category_id={:d})>
        """.format(
            self.timeframe_id,
            self.timeframe_category_id
        )
