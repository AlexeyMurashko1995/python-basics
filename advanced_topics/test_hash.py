import bcrypt


def get_password_hash(password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_bytes, salt)
    password_string = password_hash.decode('utf-8')
    return password_string