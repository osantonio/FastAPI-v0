# config/cors.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def configurar_cors(app: FastAPI) -> None:
    lista_de_origens = [
        "http://localhost:3000",
        # puedes agregar más orígenes aquí
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=lista_de_origens,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )