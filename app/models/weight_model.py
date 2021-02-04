from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from ..database import database

class BinWeight(database.Base):
    __tablename__ = "weight"

    id = Column(Integer, primary_key=True)
    datetimestamp = Column(DateTime)
    bin_weight = Column(Float)
    bin_id = Column(Integer, ForeignKey("bins.id"))

