import configuration
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, DateTime, Float, create_engine, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, nullable=False)
    key = Column(String, nullable=False)


class CollectorTable(object):
    @declared_attr
    def client(cls):
        return Column(Integer, ForeignKey('clients.id'), nullable=False)


class LocationTable(CollectorTable):
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)
    speed = Column(Float, nullable=True)
    elevation = Column(Float, nullable=True)
    the_geom = Column(Geometry('POINT'))


class UDPTable(LocationTable, Base):
    __tablename__ = 'udp'
    id = Column(Integer, primary_key=True, nullable=False)
    status = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)


class TCPTable(LocationTable, Base):
    __tablename__ = 'tcp'
    id = Column(Integer, primary_key=True, nullable=False)
    status = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)


class DB(object):
    def __init__(self):
        self._engine = None

    def connect(self):
        if self._engine:
            return
        self._engine = create_engine('postgresql://%s:%s@%s/%s' % (configuration.database_username,
                                                                   configuration.database_password,
                                                                   configuration.database_hostname,
                                                                   configuration.database_database),
                                     echo=False)

    def get_session(self):
        self.connect()
        Session = sessionmaker()
        Session.configure(bind=self._engine)
        return Session()

    def create_tables(self):
        self.connect()
        Base.metadata.create_all(self._engine)


DB = DB()
