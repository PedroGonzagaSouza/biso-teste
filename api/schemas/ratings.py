from pydantic import BaseModel

class RatingsBase(BaseModel):
    USERID: int | None = None
    MOVIEID: int | None = None
    RATING: float | None = None
    
class RatingsRequest(RatingsBase):
    ...
    
class RatingsResponse(RatingsBase):
    ...
    class Config:
        from_attributes = True