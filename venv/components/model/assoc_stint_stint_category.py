from sqlalchemy import Column, Integer,  ForeignKey
from base import DeclarativeBase


# Association table
class StintStintCategoryModel(DeclarativeBase):
    __tablename__ = 'assoc_stint_stint_category'
    __table_args__ = {'extend_existing': True}

    stint_id = Column(Integer, ForeignKey('stint.id'), primary_key=True)
    stint_category_id = Column(Integer, ForeignKey('stint_category.id'), primary_key=True)

    def __repr__(self):
        return """
        <StintStintCategoryModel(
            stint_id={:d}, 
            stint_category_id={:d})>
        """.format(
            self.stint_id,
            self.stint_category_id
        )
