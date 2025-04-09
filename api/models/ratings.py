from sqlalchemy import Integer, String, Column, REAL
from ..database.db import Base


class Ratings(Base):
    __tablename__ = "RATINGS"

    USERID: int = Column(Integer, primary_key=True, index=False)
    MOVIEID: int = Column(Integer)
    RATING: float = Column(REAL)