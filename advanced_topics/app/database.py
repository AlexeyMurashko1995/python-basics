from sqlmodel import create_engine, SQLModel


filename = 'username.db'
url = f'sqlite:///{filename}'

engine = create_engine(url)

