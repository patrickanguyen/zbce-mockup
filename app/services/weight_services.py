from sqlalchemy.orm import Session
from sqlalchemy import and_, between

from datetime import datetime
from ..models import weight_model, bininfo_model
from ..schemas import weight_schema

def weight_query_all(db : Session):
    return db.query(weight_model.BinWeight).all()


def weight_query(bin_id : int, start_timestamp : datetime, end_timestamp : datetime, db : Session):
    return db.query(weight_model.BinWeight).filter(and_(weight_model.BinWeight.bin_id == bin_id, between(weight_model.BinWeight.datetimestamp, start_timestamp, end_timestamp))).all()


def weight_add(weight: weight_schema.Weight, db : Session):
    weight_data = weight_model.BinWeight(datetimestamp=weight.timestamp, bin_weight=weight.bin_weight, bin_id=weight.bin_id)
    db.add(weight_data)
    db.commit()
    db.refresh(weight_data)

def check_bin_id(weight : weight_schema.Weight, db : Session):
    return db.query(bininfo_model.BinInfo).get(weight.bin_id) is not None


def convert_weight(weights):
    """
    Converts output from database to appropriate schema
    """
    data_list = [weight_schema.Weight(bin_weight=weight.bin_weight, timestamp=weight.datetimestamp, bin_id=weight.bin_id) for weight in weights]
    return weight_schema.BinWeight(data=data_list)