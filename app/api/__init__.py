from fastapi import APIRouter
from app.api.atleta import router as atleta_router

api_router = APIRouter()
api_router.include_router(atleta_router)
