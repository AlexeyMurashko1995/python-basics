from sqlmodel import SQLModel, Field, Session, create_engine, Relationship, select
from fastapi import FastAPI, HTTPException


app = FastAPI()

sql_file_name = 'delivery_service.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)


class Hub(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    city: str
    parcels: list['Parcel'] = Relationship(back_populates='hub')


class Parcel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tracking_number: str
    weight: float
    hub_id: int = Field(foreign_key='hub.id')
    hub: 'Hub' = Relationship(back_populates='parcels')


def init_db():
    SQLModel.metadata.create_all(engine)
    print('Database created successfully')


@app.get('/hubs')
def read_hubs_data():
    with Session(engine) as session:
        query = select(Hub)
        result = session.exec(query)
        all_hubs = result.all()
        return all_hubs


@app.post('/hubs')
def create_hub_endpoint(hub: Hub):
    with Session(engine) as session:
        session.add(hub)
        session.commit()
        session.refresh(hub)
        return hub


@app.get('/parcels')
def read_parcels_data():
    with Session(engine) as session:
        query = select(Parcel)
        result = session.exec(query)
        all_parcels = result.all()
        return all_parcels


@app.post('/parcels')
def create_parcel_endpoint(parcel: Parcel):
    with Session(engine) as session:
        session.add(parcel)
        session.commit()
        session.refresh(parcel)
        return parcel


if __name__ == '__main__':
    init_db()