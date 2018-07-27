from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.interfaces import PoolListener


class ForeignKeysListener(PoolListener):
    def connect(self, dbapi_con, con_record):
        db_cursor = dbapi_con.execute('pragma foreign_keys=ON')

class Database:

    def __init__(self):
        self.engine = create_engine(r'sqlite:///D:\practice_projects\time_management\venv\time_management.db', listeners=[ForeignKeysListener()])
        self.Session = sessionmaker(bind=self.engine)

    def process_request(self, req, resp):
        req.context['session'] = self.Session()

    def process_response(self, req, resp, resource, req_succeeded):
        req.context['session'].close()
