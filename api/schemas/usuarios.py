from pydantic import BaseModel, ValidationError


class UsuariosBase(BaseModel):
    NOME: str | None = None
    SENHA: str
    LOGIN: str
    

class UsuariosRequest(UsuariosBase):
    ...
    
class UsuariosResponse(UsuariosBase):
    USERID: int | None = None
    class Config:
        from_attributes = True
        
class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: str

    class Config:
        from_attributes = True