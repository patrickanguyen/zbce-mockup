from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..controllers import weight_controller
from ..schemas import weight_schema
from ..database import database

router = APIRouter()

@router.get("/weight-all/", response_model=weight_schema.BinWeight)
def get_all_weights(db: Session = Depends(database.get_db)):
    return weight_controller.get_all_weights(db)

