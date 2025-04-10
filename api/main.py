from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 
from .routes.usuarios import router as usuarios_router
from .routes.filmes import router as filmes_router
from .routes.ratings import router as ratings_router
from .routes.tratamento import router as tratamento_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router)
app.include_router(ratings_router)
app.include_router(filmes_router)
app.include_router(tratamento_router)
