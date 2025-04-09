from fastapi import FastAPI
 
from .routes.usuarios import router as usuarios_router
from .routes.filmes import router as filmes_router
from .routes.ratings import router as ratings_router
from .routes.tratamento import router as tratamento_router
# from .database.db import engine, Base
# from controllers.usuarios import UsuariosController
# Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(usuarios_router)
app.include_router(ratings_router)
app.include_router(filmes_router)
app.include_router(tratamento_router)

# app.include_router(filmes_router)

# @app.delete("/api/usuario/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def deletaUsuario(id: int, db: Session = Depends(get_db)):
#     """
#     Deleta um usuário pelo ID.
#     """
#     usuario = db.query(Usuarios).filter(Usuarios.USERID == id).first()
#     if not usuario:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
#     db.delete(usuario)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.post("/api/teste", response_model=UsuariosResponse, status_code=status.HTTP_201_CREATED)
# async def teste(usuario: UsuariosBase):
#     """
#     Teste de criação de usuário.
#     """
#     try:
#         usuariosBody = Usuarios(
#             NOME=usuario.NOME,
#             SENHA=usuario.SENHA,
#             LOGIN=usuario.LOGIN
#         )
#         conn = sqlite3.connect('./filmes.db')
#         cur = conn.cursor()
#         cur.execute(f"INSERT INTO USUARIOS (NOME, SENHA, LOGIN) VALUES (?, ?, ?)", (usuariosBody.NOME, usuariosBody.SENHA, usuariosBody.LOGIN))
#         conn.commit()
#         conn.close()
#         return {
#             "message": "Usuário criado com sucesso!"
#         }
#     except sqlite3.Error as e:
#         return {
#             "message": "Erro ao criar usuário",
#             "error": str(e)
#         }

# @app.post("/api/usuario", response_model=UsuariosResponse, status_code=status.HTTP_201_CREATED)
# async def criaUsuario(usuario: UsuariosBase, db: Session = Depends(get_db)):
#     """
#     Cria um novo usuário no banco de dados.
#     """
#     db_usuario = Usuarios(
#         NOME=usuario.NOME,
#         SENHA=usuario.SENHA,
#         LOGIN=usuario.LOGIN
#     )
#     db.add(db_usuario)
#     db.commit()
#     db.refresh(db_usuario)
#     return db_usuario

# @app.get("/api/usuario/{id}", response_model=UsuariosResponse, status_code=status.HTTP_200_OK)
# async def buscaUsuario(id: int, db: Session = Depends(get_db)):
#     """
#     Busca um usuário pelo ID.
#     """
#     usuario = db.query(Usuarios).filter(Usuarios.USERID == id).first()
#     if not usuario:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
#     return usuario

# @app.get("/api/usuario", response_model=list[UsuariosResponse], status_code=status.HTTP_200_OK)
# async def buscaUsuarios(db: Session = Depends(get_db)):
#     """
#     Busca todos os usuários.
#     """
#     usuarios = db.query(Usuarios).all()
#     return usuarios