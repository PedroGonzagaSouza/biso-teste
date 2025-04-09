from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from ..database.db import get_db

from ..models.ratings import Ratings
from ..schemas.ratings import RatingsBase, RatingsResponse, RatingsRequest
from sqlalchemy.sql import text

class RatingsController: 
    
    async def getAll(db: Session = Depends(get_db)):
        try:
            ratings = db.execute(text("SELECT * FROM RATINGS")).fetchall()
            if not ratings:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum rating encontrado")
            return ratings
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    async def getRatingByUserAndMovie(usuario_id: int, movie_id: int, db: Session = Depends(get_db)):
        try:
            rating = db.query(Ratings).filter(Ratings.USERID == usuario_id, Ratings.MOVIEID == movie_id).first()
            if not rating:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
            return rating
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    async def createRating(rating: RatingsRequest, db: Session = Depends(get_db)):
        try:
            new_rating = Ratings(**rating.model_dump())
            db.add(new_rating)
            db.commit()
            db.refresh(new_rating)
            return new_rating
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        