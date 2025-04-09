from pydantic import BaseModel, ValidationError


class UsuariosBase(BaseModel):
    NOME: str
    SENHA: str
    LOGIN: str
    

class UsuariosRequest(UsuariosBase):
    ...
    
class UsuariosResponse(UsuariosBase):
    USERID: int | None = None
    class Config:
        from_attributes = True