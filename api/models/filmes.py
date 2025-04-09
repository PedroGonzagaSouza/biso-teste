from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, Boolean, Text, Float

from ..database.db import Base

class Filmes(Base):
    __tablename__ = "FILMES"
    
    MOVIEID: int = Column(Integer, primary_key=True, index=True, unique=True)
    TITLE: str = Column(String(255))
    GENRES: str = Column(String(255))
    YEAR: int = Column(Integer)
   