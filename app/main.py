from fastapi import FastAPI
import uvicorn
from .routers import weight_router
from .services import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(docs_url="/", redoc_url=None, title="ZBCE API")

app.include_router(weight_router.router)


