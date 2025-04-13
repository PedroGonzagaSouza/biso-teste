from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response

from ..models.filmes import Filmes
from ..schemas.filmes import FilmesResponse, FilmesRequest

from ..models.ratings import Ratings
from ..schemas.ratings import RatingsBase, RatingsResponse, RatingsRequest

from ..database.db import get_db
from sqlalchemy.sql import text
class FilmesControllers:
    
    async def getAll(db: Session = Depends(get_db)):
        """
        Get all movies from the database.
        """
        try:
            filmes = db.execute(text("SELECT * FROM FILMES")).fetchall()
            if not filmes:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum filme encontrado")
            return filmes
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    async def getFilmes(db: Session, offset: int = 0, limit: int = 10) -> list[Filmes]:
      #Get todos os filmes com paginação
        filmes = db.query(Filmes).offset(offset).limit(limit).all()
        total = db.query(Filmes).count()
        return {"total": total, "filmes": filmes}
    
    async def getFilmesById(db: Session, id: int) -> Filmes:
        #get filme por id
        filme = db.query(Filmes).filter(Filmes.MOVIEID == id).first()
        if not filme:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
        return filme
    
    async def getFilmesByTitle(db: Session, titulo: str) -> list[Filmes]:
       #get filme por titulo
       #manda um LIKE pro SQL e traz uma lista com os nomes parecidos, precisa de atenção
        filmes = db.query(Filmes).filter(Filmes.TITLE.ilike(f"%{titulo}%")).all()
        if not filmes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
        return filmes
    
    async def getFilmesByUser(db: Session, usuario_id: int) -> list[Filmes]:
        #get filme por usuario
        filmes = db.query(Ratings).filter(Ratings.USERID == usuario_id).all()
        if not filmes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
        return filmes