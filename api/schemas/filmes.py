from pydantic import BaseModel, ConfigDict, AliasPath, Field, ValidationError

class FilmesBase(BaseModel):
    MOVIEID: int
    TITLE: str
    GENRES: str 
    YEAR: int
    
class FilmesRequest(FilmesBase):
    ...
    
class FilmesResponse(FilmesBase):
    # model_config = ConfigDict(from_attributes=True)
    
    class Config:
        from_attributes = True