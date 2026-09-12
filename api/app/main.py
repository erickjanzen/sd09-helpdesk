from fastapi import FastAPI
from app.controllers.usuario_controller import router as usuario_router


app = FastAPI()

app.include_router(usuario_router)

# executar
# uvicorn app.main:app --reload