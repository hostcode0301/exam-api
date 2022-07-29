from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import config
from app.api.router import router as api_router
from app.api.errors.validation_error import http422_error_handler
from app.api.errors.http_error import http_error_handler

def get_application():
    application = FastAPI(
        title=config.app_name,
        description=config.description,
        debug=config.debug,
        docs_url=f'{config.api_prefix}/docs',
        redoc_url=f'{config.api_prefix}/redoc',
        openapi_url=f'{config.api_prefix}/openapi.json',
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=config.origin,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(
        HTTPException,
        http_error_handler,
    )

    application.add_exception_handler(
        RequestValidationError,
        http422_error_handler,
    )

    application.include_router(api_router, prefix=config.api_prefix)

    return application

app = get_application()