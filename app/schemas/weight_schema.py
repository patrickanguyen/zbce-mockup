from pydantic import BaseModel
from typing import List
from datetime import datetime

class Weight(BaseModel):
    bin_id : int 
    bin_weight : float 
    timestamp : datetime

    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2015-11-04 15:06:25",
                "bin_weight": 25,
                "bin_id": 1
                }
        }

class BinWeight(BaseModel):
    data : List[Weight]

    class Config:
        orm_mode = True
