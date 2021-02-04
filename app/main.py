from fastapi import FastAPI
import uvicorn
from .routers import weight_router
from .database import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(weight_router.router)


