from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from datetime import datetime
from ..controllers import weight_controller
from ..schemas import schema, weight_schema
from ..services import database

router = APIRouter(tags=["Weight"])

@router.get("/weight-all/", response_model=weight_schema.BinWeight)
def get_all_weights(db: Session = Depends(database.get_db)):
    #TODO: Fix the response of timestamp because it has a "T" "2015-11-04T15:06:25" because of the __str__ of datetime
    return weight_controller.get_all_weights(db)

@router.get("/weight/", response_model=weight_schema.BinWeight)
def get_weight(bin_id : int, start_timestamp : datetime, end_timestamp : datetime, db : Session = Depends(database.get_db)):
    #TODO: Error checking of start_timestamp and end_timestamp
    return weight_controller.get_weight(bin_id, start_timestamp, end_timestamp, db)

@router.post("/weight/", status_code=status.HTTP_201_CREATED, response_model=schema.Message, 
responses={
        status.HTTP_201_CREATED : {"description" : "All of the weights have been successfully added to the database",
                "content" : {
                    "application/json" : {
                        "example" : {"message" : "Successfully posted weight"}
                    }
                }
        },
        status.HTTP_404_NOT_FOUND : {"description" : "The bin ID is provided is invalid and does not exist in the database",
                "content" : {
                    "application/json" : {
                        "example" : {"message": "Invalid bin_id"}
                    }
                },
                "model" : schema.Message
            }
        }
)
def post_weight(weights : weight_schema.BinWeight, db : Session = Depends(database.get_db)):
    return weight_controller.add_weight(weights, db)