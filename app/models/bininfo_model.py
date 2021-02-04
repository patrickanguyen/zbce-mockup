from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..services import database

class BinInfo(database.Base):
    __tablename__ = "bins"

    id = Column(Integer, primary_key=True)
    ip_address = Column(String(64), unique=True)
    bin_height = Column(Integer)
    location = Column(String(64))
    bin_type = Column(String(64))
    waste_metrics = Column(String(64))

    # fullnesses = relationship('BinFullness', backref='bin',lazy='dynamic')
    weights = relationship('BinWeight', backref='bin',lazy='dynamic')
    # usages = relationship('BinUsage', backref='bin',lazy='dynamic')