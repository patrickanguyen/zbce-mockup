from sqlalchemy.orm import Session

from ..models import weight_model

def weight_query_all(db : Session):
    return db.query(weight_model.BinWeight).all()
