from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from .config import API_STR
from .db import connect_to_mongo, close_mongo_connection
from .endpoints import router
from .errors import http_error_handler, http_422_error_handler

app = FastAPI()

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

app.include_router(router, prefix=API_STR)
