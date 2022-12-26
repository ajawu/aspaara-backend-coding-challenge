from fastapi import APIRouter

from app.api.api_v1.endpoints import plan

api_router = APIRouter()
api_router.include_router(plan.router, prefix="/plan", tags=["plan"])
