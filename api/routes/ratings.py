from fastapi import APIRouter, Depends, HTTPException, status, Response
from ..database.db import get_db
from sqlalchemy.orm import Session

from ..controllers.ratings import RatingsController
from ..schemas.ratings import RatingsResponse, RatingsRequest

router = APIRouter(
    prefix="/api/rating",
    tags=["Ratings"]
)

@router.get("/{usuario_id}/{movie_id}", response_model=RatingsResponse, status_code=status.HTTP_200_OK)
async def busca_rating(usuario_id: int, movie_id: int, db: Session = Depends(get_db)):
    try:
        rating = await RatingsController.getRatingByUserAndMovie(usuario_id, movie_id, db)
        return rating
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.post("/", response_model=RatingsResponse, status_code=status.HTTP_201_CREATED)
async def cria_rating(rating: RatingsRequest, db: Session = Depends(get_db)):
    try:
        new_rating = await RatingsController.createRating(rating, db)
        return new_rating
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))