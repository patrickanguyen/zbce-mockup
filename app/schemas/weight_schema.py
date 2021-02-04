from pydantic import BaseModel
from typing import List
from datetime import datetime

class WeightBase(BaseModel):
    bin_id : int 

class WeightIn(WeightBase):
    start_timestamp : datetime
    end_timestamp : datetime

class Weight(BaseModel):
    bin_id : int
    bin_weight : float 
    timestamp : datetime 

class BinWeight(BaseModel):
    data : List[Weight]