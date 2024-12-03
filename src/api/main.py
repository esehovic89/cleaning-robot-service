from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from configuration.logger import Logger

app = FastAPI()

APPLICATION_UNHANDLED_EXCEPTION_TEXT = "Internal server error"


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exception:
        logger = Logger.get_logger()
        logger.exception(str(exception))
        return Response("Internal server error", status_code=500)


app.middleware("http")(catch_exceptions_middleware)
