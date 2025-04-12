from fastapi import APIRouter, Depends, HTTPException, status, Response
from ..database.db import get_db
from sqlalchemy.orm import Session

from ..controllers.tratamento import TratamentoController
from ..controllers.ratings import RatingsController
from ..controllers.filmes import FilmesControllers
from ..schemas.filmes import FilmesResponse, FilmesRequest

router = APIRouter(
    prefix="/api/filme",
    tags=["Filmes"]
)

@router.get("/all", response_model=list[FilmesResponse], status_code=status.HTTP_200_OK)
async def busca_filmes(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        filmes = await FilmesControllers.getFilmes(db, offset, limit)
        return filmes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/{id}", response_model=FilmesResponse, status_code=status.HTTP_200_OK)
async def busca_filme_id(id: int, db: Session = Depends(get_db)):
    try:
        filme = await FilmesControllers.getFilmesById(db, id)
        return filme
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/title/{titulo}", response_model=list[FilmesResponse], status_code=status.HTTP_200_OK)
async def busca_filme_titulo(titulo: str, db: Session = Depends(get_db)):
    try:
        filme = await FilmesControllers.getFilmesByTitle(db, titulo)
        return filme
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/{usuario_id}/recomendacoes", response_model=list[FilmesResponse], status_code=status.HTTP_200_OK)
async def recomendacao_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        filmes = await FilmesControllers.getAll(db)
        ratings = await RatingsController.getAll(db)
        recomendacoes = await TratamentoController.tratamento_usuario(filmes, ratings, usuario_id)
        return recomendacoes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))