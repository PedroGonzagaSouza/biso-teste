from fastapi import APIRouter, Depends, HTTPException, status, Response

from sqlalchemy.orm import Session
from ..database.db import get_db
from ..controllers.tratamento import TratamentoController
from ..controllers.ratings import RatingsController
from ..controllers.filmes import FilmesControllers

router = APIRouter(
    prefix="/api/tratamento",
    tags=["Tratamento"]
)

@router.get("/recomendacao/{filme}", status_code=status.HTTP_200_OK)
async def recomendacao(filme: str, db: Session = Depends(get_db)):
    try:
        filmes = await FilmesControllers.getAll(db)
        ratings = await RatingsController.getAll(db)
        recomendacoes = await TratamentoController.tratamento(filmes, ratings, filme)
        return recomendacoes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/filmes/{usuario_id}/recomendacoes", status_code=status.HTTP_200_OK)
async def recomendacao_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        filmes = await FilmesControllers.getAll(db)
        ratings = await RatingsController.getAll(db)
        recomendacoes = await TratamentoController.tratamento_usuario(filmes, ratings, usuario_id)
        return recomendacoes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))