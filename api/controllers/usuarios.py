from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from ..database.db import get_db

from ..models.usuarios import Usuarios
from ..schemas.usuarios import UsuariosBase, UsuariosResponse, UsuariosRequest

class UsuariosController: 

    async def criaUsuario(usuario: UsuariosRequest, db: Session = Depends(get_db)):
        try:
            usuario_db = Usuarios(**usuario.model_dump())
            db.add(usuario_db)
            db.commit()
            db.refresh(usuario_db)
            return usuario_db
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    async def buscaUsuarioId(usuario_id: int, db: Session = Depends(get_db)):
        try:
            usuario = db.query(Usuarios).filter(Usuarios.USERID == usuario_id).first()
            if not usuario:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
            return usuario
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            
    async def buscaUsuarios(db: Session = Depends(get_db)):
        try:
            usuarios = db.query(Usuarios).all()
            if not usuarios:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum usuário encontrado")
            return usuarios
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def buscaUsuarioLogin(login: str, db: Session = Depends(get_db)):
        try:
            usuario = db.query(Usuarios).filter(Usuarios.LOGIN == login).first()
            if not usuario:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
            return usuario
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))