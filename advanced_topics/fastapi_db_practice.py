from sqlmodel import SQLModel, Session, create_engine, Field
from fastapi import FastAPI


app = FastAPI()


class Bike(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    model: str = Field(min_length=2)
    type: str
    price: int = Field(gt=0)


sqlite_filename = 'database.db'
url = f'sqlite:///{sqlite_filename}'

engine = create_engine(url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event('startup')
def on_startup():
    create_db_and_tables()


@app.post('/bikes')
def create_bikes(bike_in: Bike):
    with Session(engine) as session:
        session.add(bike_in)
        session.commit()
        session.refresh(bike_in)
        return bike_in