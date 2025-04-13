from fastapi import APIRouter, Depends, HTTPException, status, Response
from ..database.db import get_db
from sqlalchemy.orm import Session

from ..controllers.tratamento import TratamentoController
from ..controllers.ratings import RatingsController
from ..controllers.filmes import FilmesControllers
from ..schemas.filmes import FilmesResponse, FilmesRequest, FilmesPaginatedResponse

router = APIRouter(
    prefix="/api/filme",
    tags=["Filmes"]
)

@router.get("/all/{offset}/{limit}", response_model=FilmesPaginatedResponse, status_code=status.HTTP_200_OK)
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
    
@router.get("/title/{titulo}/{offset}/{limit}", response_model=FilmesPaginatedResponse, status_code=status.HTTP_200_OK)
async def busca_filme_titulo(titulo: str, offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        filme = await FilmesControllers.getFilmesByTitle(db, titulo, offset, limit)
        return filme
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/recomendacao/colaborativa/{usuario_id}", status_code=status.HTTP_200_OK)
async def recomendacao_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        filmes = await FilmesControllers.getAll(db)
        ratings = await RatingsController.getAll(db)
        recomendacoes = await TratamentoController.tratamento_usuario(filmes, ratings, usuario_id)
        # recomendacoes = await TratamentoController.recomendacao_hibrida(filmes, ratings, usuario_id)
        return recomendacoes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{usuario_id}/recomendacoes", status_code=status.HTTP_200_OK)
async def recomendacao_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        filmes = await FilmesControllers.getAll(db)
        ratings = await RatingsController.getAll(db)
        # recomendacoes = await TratamentoController.tratamento_usuario(filmes, ratings, usuario_id)
        # recomendacoes = await TratamentoController.recomendacao_hibrida(filmes, ratings, usuario_id)
        recomendacoes = await TratamentoController.recomendacao_hibrida_conteudo(filmes, ratings, usuario_id)
        
        
        return recomendacoes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/recomendacao/conteudo/{usuario_id}", status_code=status.HTTP_200_OK)
async def recomendacao(usuario_id: int, db: Session = Depends(get_db)):
    try:
        filmes = await FilmesControllers.getAll(db)
        ratings = await RatingsController.getAll(db)
        recomendacoes = await TratamentoController.filtragem_por_conteudo(filmes, ratings, usuario_id)
        return recomendacoes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{usuario_id}/assistidos", response_model=list[FilmesResponse], status_code=status.HTTP_200_OK)
async def filmes_assistidos(usuario_id: int, db: Session = Depends(get_db)):
    try:
        assistidos = await FilmesControllers.getFilmesByUser(db, usuario_id)
        return assistidos
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))