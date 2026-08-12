from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()

def get_password_hash(password: str):
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str):
    return PasswordHash.verify(password, hashed_password)