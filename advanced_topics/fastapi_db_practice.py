from sqlmodel import SQLModel, Session, create_engine
from fastapi import FastAPI


app = FastAPI()

sqlite_filename = 'database.db'
url = f'sqlite:///{sqlite_filename}'

engine = create_engine(url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event('startup')
def on_startup():
    create_db_and_tables()
