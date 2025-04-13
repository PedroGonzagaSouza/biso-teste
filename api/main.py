from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 
from .routes.usuarios import router as usuarios_router
from .routes.filmes import router as filmes_router
from .routes.ratings import router as ratings_router
from .routes.tratamento import router as tratamento_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import sqlite3
import pandas as pd

def populate_database():
    filmes = pd.read_csv('./data/Filmes.csv')
    ratings = pd.read_csv('./data/Ratings.csv')
    tags = pd.read_csv('./data/Tags.csv')
    # print(filmes.head(10))
    conn = sqlite3.connect('./filmes.db')
    c = conn.cursor()
        
    c.execute("CREATE TABLE FILMES (MOVIEID INTEGER,TITLE TEXT,GENRES TEXT,YEAR INTEGER)")
    c.execute("CREATE TABLE RATINGS (USERID, MOVIEID, RATING )")
    c.execute("CREATE TABLE TAGS (MOVIEID INTEGER,TAG TEXT)")
    c.execute("CREATE TABLE USUARIOS (USERID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT, SENHA TEXT, LOGIN TEXT UNIQUE)")
    for i in range(650):
        login = f"LOGIN_UNICO_{i}"
        c.execute("SELECT COUNT(*) FROM USUARIOS WHERE LOGIN = ?", (login,))
        if c.fetchone()[0] == 0:  # Se não existir, insere
            c.execute("INSERT OR IGNORE INTO USUARIOS (NOME, SENHA, LOGIN) VALUES (?, ?, ?)", (f"TESTE{i}", f"TESTE{i}", login))

    filmes.to_sql('FILMES', conn, if_exists='append', index=False, dtype={'MOVIEID': 'INTEGER', 'TITLE': 'TEXT', 'GENRES': 'TEXT', 'YEAR': 'INTEGER'})
    ratings.to_sql('RATINGS', conn, if_exists='append', index=False, dtype={'USERID': 'INTEGER', 'MOVIEID': 'INTEGER', 'RATING': 'REAL'})
    tags.to_sql('TAGS', conn, if_exists='append', index=False, dtype={'MOVIEID': 'INTEGER', 'TAG': 'TEXT'})
    conn.commit()
    conn.close() 
@app.on_event("startup")
def on_startup():
    populate_database()

app.include_router(usuarios_router)
app.include_router(ratings_router)
app.include_router(filmes_router)
app.include_router(tratamento_router)
