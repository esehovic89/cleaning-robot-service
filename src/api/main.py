from fastapi import APIRouter, FastAPI

from src.api.cleaning_robot_endpoints import router
from src.api.utils import catch_exceptions_middleware

app = FastAPI()

app.middleware("http")(catch_exceptions_middleware)

api_router = APIRouter()
api_router.include_router(router)
app.include_router(api_router)
