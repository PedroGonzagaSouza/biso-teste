from pydantic import BaseModel

class RatingsBase(BaseModel):
    USERID: int
    MOVIEID: int 
    RATING: float 
    
class RatingsRequest(RatingsBase):
    ...
    
class RatingsResponse(RatingsBase):
    RATING: float
    
    class Config:
        from_attributes = True