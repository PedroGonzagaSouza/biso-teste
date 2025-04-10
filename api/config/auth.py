from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

#configs do jwt
SECRET_KEY = "biso-teste"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#hashing de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#gerador de hash a partir da senha
def hashPassword(password: str) -> str:
    return pwd_context.hash(password)

#verifica se a senha é válida
def verifyPassword(plainPassword: str, hashedPassword: str) -> bool:
    return pwd_context.verify(plainPassword, hashedPassword)

#criar token de acesso
def createAccessToken(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#verifica se o token é válido
def verifyAccessToken(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None