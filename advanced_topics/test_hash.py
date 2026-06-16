import bcrypt


def get_password_hash(password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password_bytes, salt)
    clean_password = password_hashed.decode('utf-8')
    return clean_password

