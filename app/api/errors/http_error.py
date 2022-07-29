from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.models.schemas.responses import ResponseModel

async def http_error_handler(
    _: Request,
    exc: HTTPException,
) -> JSONResponse:
    return JSONResponse(
        ResponseModel(
            code=exc.status_code,
            message=exc.detail,
        ).dict(),
        status_code=exc.status_code,
    )