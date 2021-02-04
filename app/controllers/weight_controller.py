from sqlalchemy.orm import Session

from ..models import weight_model
from ..schemas import weight_schema

def get_weight(db : Session, weight : weight_schema.WeightIn):
    return db.query(weight_model.BinWeight).filter()