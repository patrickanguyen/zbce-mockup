from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import weight_controller
from ..schemas import weight_schema
from ..database import database

router = APIRouter()

@router.get("/weight/")
def get_weight(weight : weight_schema.WeightIn, db: Session = Depends(database.get_db)):
    return weight_controller.get_weight(db, weight)

