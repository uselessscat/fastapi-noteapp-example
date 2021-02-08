from fastapi import FastAPI

from app.bootstrap import AppBuilder
from app.config import Settings

app = AppBuilder \
    .with_environment_settings() \
    .build()
