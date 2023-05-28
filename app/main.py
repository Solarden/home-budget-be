from fastapi import FastAPI

from app.api.routes import api_router
from app.core import settings


def get_application() -> FastAPI:
    """Create FastAPI application."""
    application = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
    application.include_router(api_router, prefix=settings.API_PREFIX)

    return application


app = get_application()
