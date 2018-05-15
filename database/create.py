from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text

from database.config import USER, PASSWORD, HOST, PORT, DATABASE

engine = create_engine('mysql://{0}:{1}@{2}:{3}'.format(USER, PASSWORD, HOST, PORT))
engine.execute("CREATE DATABASE IF NOT EXISTS {0} ".format(DATABASE))
db_engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}'.format(USER, PASSWORD, HOST, PORT, DATABASE))

Base = declarative_base()


class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Text)
    scan_id = Column(Text)
    report_filename = Column(Text)
    events_num = Column(Integer)
    verbose = Column(Integer)
    api_flag = Column(Integer)
    report_type = Column(Text)
    graph_flag = Column(Text)
    category = Column(Text)
    profile = Column(Text)
    scan_method = Column(Text)
    language = Column(Text)
    scan_cmd = Column(Text)
    ports = Column(Text)

    def __repr__(self):
        return "<Report(id='%s', scan_id='%s', date='%s')>" % (self.id, self.scan_id, self.date)


class HostsLog(Base):
    __tablename__ = 'hosts_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(Text)
    date = Column(Text)
    scan_id = Column(Text)
    scan_cmd = Column(Text)
    username = Column(Text)
    password = Column(Text)
    description = Column(Text)
    port = Column(Integer)
    category = Column(Text)
    type = Column(Text)

    def __repr__(self):
        return "<HostsLog(id='%s', host='%s', date='%s')>" % (self.id, self.host, self.date)


Base.metadata.create_all(db_engine)