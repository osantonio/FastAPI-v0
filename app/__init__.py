# app/__init__.py

from fastapi import FastAPI
from app.config.cors import configurar_cors

# import routers
from app.api.v1.endpoint import main_router


def create_app():
    app = FastAPI()

    # Configurar CORS
    configurar_cors(app)

    # include routers
    app.include_router(main_router)
    return app
