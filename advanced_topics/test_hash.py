import bcrypt


def get_password_hash(password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_bytes, salt)
    hash_string = password_hash.decode('utf-8')
    return hash_string


def verify_password(password: str, hash_string: str):
    password_bytes = password.encode('utf-8')
    hash_bytes = hash_string.encode('utf-8')
    verification = bcrypt.checkpw(password_bytes, hash_bytes)
    return verification

