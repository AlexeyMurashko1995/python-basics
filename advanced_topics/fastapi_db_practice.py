from sqlmodel import SQLModel, Session, create_engine, Field, select
from fastapi import FastAPI, HTTPException


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


@app.get('/bikes')
def get_bikes():
    with Session(engine) as session:
        query = select(Bike)
        result = session.exec(query)
        all_bikes = result.all()
        return all_bikes


@app.get('/bikes/{bike_id}')
def get_bike(bike_id: int):
    with Session(engine) as session:
        bike = session.get(Bike, bike_id)
        if bike:
            return bike
        else:
            raise HTTPException(status_code=404,detail='Bike not found')


@app.patch('/bikes/{bike_id}')
def update_bike(bike_id: int, bike_data: Bike):
    with Session(engine) as session:
        target_bike = session.get(Bike, bike_id)
        if not target_bike:
            raise HTTPException(status_code=404, detail='Bike not found')
        else:
            target_bike.model = bike_data.model
            target_bike.type = bike_data.type
            target_bike.price = bike_data.price
            session.commit()
            session.refresh(target_bike)
            return target_bike


@app.delete('/bikes/{bike_id}')
def delete_bike(bike_id: int):
    with Session(engine) as session:
        target_bike = session.get(Bike, bike_id)
        if target_bike:
            session.delete(target_bike)
            session.commit()
            return {'message': 'Bike successfully deleted'}
        else:
            raise HTTPException(status_code=404, detail='Bike not found')