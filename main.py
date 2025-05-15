from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

import home

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

app.include_router(home.router)

templates = Jinja2Templates(directory=".")
