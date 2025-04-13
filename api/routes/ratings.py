from fastapi import APIRouter, Depends, HTTPException, status, Response
from ..database.db import get_db
from sqlalchemy.orm import Session

from ..controllers.ratings import RatingsController
from ..schemas.ratings import RatingsResponse, RatingsRequest

router = APIRouter(
    prefix="/api/ratings",
    tags=["Ratings"]
)

@router.get("/all", response_model=list[RatingsResponse], status_code=status.HTTP_200_OK)
async def busca_todos_ratings(db: Session = Depends(get_db)):
    try:
        ratings = await RatingsController.getAll(db)
        return ratings
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/user/{usuario_id}", response_model=list[RatingsResponse], status_code=status.HTTP_200_OK)
async def busca_ratings_por_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        ratings = await RatingsController.getAllRatingsByUser(usuario_id, db)
        return ratings
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/user/{usuario_id}/filme/{movie_id}", response_model=RatingsResponse, status_code=status.HTTP_200_OK)
async def busca_rating(usuario_id: int, movie_id: int, db: Session = Depends(get_db)):
    try:
        rating = await RatingsController.getRatingByUserAndMovie(usuario_id, movie_id, db)
        print(rating)
        if not rating:
            return None
        return rating
    except Exception as e:
        return {"ratings": None}
    
@router.post("/", response_model=RatingsResponse, status_code=status.HTTP_201_CREATED)
async def cria_rating(rating: RatingsRequest, db: Session = Depends(get_db)):
    try:
        new_rating = await RatingsController.createRating(rating, db)
        return new_rating
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put("/", response_model=RatingsResponse, status_code=status.HTTP_200_OK)
async def atualiza_rating(rating: RatingsRequest, db: Session = Depends(get_db)):
    try:
        updated_rating = await RatingsController.updateRating(rating, db)
        return updated_rating
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.delete("/{usuario_id}/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleta_rating(usuario_id: int, movie_id: int, db: Session = Depends(get_db)):
    try:
        await RatingsController.deleteRating(usuario_id, movie_id, db)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))