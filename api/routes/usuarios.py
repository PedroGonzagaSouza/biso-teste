from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session 
from ..schemas.usuarios import UsuariosResponse, UsuariosRequest, LoginResponse
from ..database.db import get_db
from ..controllers.usuarios import UsuariosController

from ..config.auth import hashPassword, verifyPassword, createAccessToken, verifyAccessToken
router = APIRouter(
    prefix="/api/usuario",
    tags=["usuarios"],  
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/usuario/login")

def getCurrentUser(token: str = Depends(oauth2_scheme)):
    try:
        payload = verifyAccessToken(token)
        if payload is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
        return payload
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

@router.get("/me", response_model=UsuariosResponse, status_code=status.HTTP_200_OK)
async def getProfile(currentUser: dict = Depends(getCurrentUser)):
    return {"login": currentUser["sub"]}

@router.get("/all", response_model=list[UsuariosResponse], status_code=status.HTTP_200_OK)
async def busca_usuarios(db: Session = Depends(get_db)):
    try:
        usuarios = await UsuariosController.buscaUsuarios(db)
        return usuarios
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{usuario_id}", response_model=UsuariosResponse, status_code=status.HTTP_200_OK)
async def busca_usuario_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        usuario = await UsuariosController.buscaUsuarioId(usuario_id, db)
        return usuario
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# @router.post("/create", response_model=UsuariosResponse, status_code=status.HTTP_201_CREATED)
# async def cria_usuario(usuario: UsuariosRequest, db: Session = Depends(get_db)):
#     try:
#         return await UsuariosController.criaUsuario(usuario, db)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
#post com hash
@router.post("/create/hash", response_model=UsuariosResponse, status_code=status.HTTP_201_CREATED)
async def registraUsuario(usuario: UsuariosRequest, db: Session = Depends(get_db)):
    try:
        hashedPassword = hashPassword(usuario.SENHA)
        novoUsuario = UsuariosRequest(
            NOME=usuario.NOME,
            LOGIN=usuario.LOGIN,
            SENHA=hashedPassword,
        )
        return await UsuariosController.criaUsuario(novoUsuario, db)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    
@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(usuario: UsuariosRequest, db: Session = Depends(get_db)):
    try:
        user = await UsuariosController.buscaUsuarioLogin(usuario.LOGIN, db)
        if not user or not verifyPassword(usuario.SENHA, user.SENHA):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário ou senha inválidos")
        accessToken = createAccessToken(data={"sub": user.LOGIN})
        return {"access_token": accessToken, "token_type": "bearer", "user": user.LOGIN}
    except Exception as e:
        raise e
# @router.post("/login", response_model=UsuariosResponse, status_code=status.HTTP_200_OK)
# async def login(usuario: UsuariosRequest, db: Session = Depends(get_db)):
#     try:
#         user = await UsuariosController.buscaUsuarioLogin(usuario.LOGIN, db)
#         if not user or not verifyPassword(usuario.SENHA, user.SENHA):
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário ou senha inválidos")
#         accessToken = createAccessToken(data={"sub": user.LOGIN})
#         return {"access_token": accessToken, "token_type": "bearer", "user": user.LOGIN}
#     except Exception as e:
#         raise e