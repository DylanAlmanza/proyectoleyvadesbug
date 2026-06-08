import bcrypt
import re

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def validar_curp(curp: str) -> bool:
    return bool(re.fullmatch(r"[A-Z0-9]{18}", curp))

def validar_telefono(tel: str) -> bool:
    return bool(re.fullmatch(r"\d{10}", tel))
