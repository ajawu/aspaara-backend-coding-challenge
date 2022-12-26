from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError

from app import exception_handlers
from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

app.add_exception_handler(
    IntegrityError, handler=exception_handlers.integrity_error_handler
)
