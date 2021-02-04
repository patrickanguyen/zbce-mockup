from sqlalchemy.orm import Session

from ..database import weight_database
from ..models import weight_model
from ..schemas import weight_schema

def get_all_weights(db : Session):
    weights = weight_database.weight_query_all(db)
    data_list = [weight_schema.Weight(bin_weight=weight.bin_weight, timestamp=weight.datetimestamp, bin_id=weight.bin_id) for weight in weights]
    return weight_schema.BinWeight(data=data_list)