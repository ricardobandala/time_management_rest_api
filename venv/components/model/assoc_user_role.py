from sqlalchemy import Column, Integer,  ForeignKey
from base import DeclarativeBase


# Association table
class UserRoleModel(DeclarativeBase):
    __tablename__ = 'user_role'
    __table_args__ = {'extend_existing': True}

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('resource.id'), primary_key=True)

    def __repr__(self):
        return """
        <UserRoleModel(
            user_id={:d}, 
            role_id={:d})>
        """.format(
            self.user_id,
            self.role_id
        )
