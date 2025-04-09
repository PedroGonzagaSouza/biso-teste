from sqlalchemy import Integer, String, Column

from ..database.db import Base

class Usuarios(Base):
    __tablename__ = "USUARIOS"
    
    USERID: int = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    NOME: str = Column(String(), nullable=False)
    SENHA: str = Column(String(), nullable=False)
    LOGIN: str = Column(String(), unique=True, nullable=False)
