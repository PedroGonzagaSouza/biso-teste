from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session 
from ..schemas.usuarios import UsuariosResponse, UsuariosRequest
from ..database.db import get_db
from ..controllers.usuarios import UsuariosController


router = APIRouter(
    prefix="/api/usuario",
)


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

@router.post("/create", response_model=UsuariosResponse, status_code=status.HTTP_201_CREATED)
async def cria_usuario(usuario: UsuariosRequest, db: Session = Depends(get_db)):
    try:
        return await UsuariosController.criaUsuario(usuario, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))