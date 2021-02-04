from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from ..services import weight_services
from ..models import weight_model
from ..schemas import schema, weight_schema

def get_all_weights(db : Session):
    weights = weight_services.weight_query_all(db)
    return weight_services.convert_weight(weights)

def get_weight(bin_id : int, start_timestamp : datetime, end_timestamp : datetime, db : Session):
    weights = weight_services.weight_query(bin_id, start_timestamp, end_timestamp, db)
    return weight_services.convert_weight(weights)

def add_weight(weights : weight_schema.BinWeight, db : Session):
    for weight in weights.data:
        # Add all weights if contains valid bin_id
        if weight_services.check_bin_id(weight, db):
            weight_services.weight_add(weight, db)
        else:
            return JSONResponse(status_code=404, content={"message" : "Invalid bin_id"})
    # If all weights are succesfully added, return success message
    return {"message" : "Successfully posted weight"}

