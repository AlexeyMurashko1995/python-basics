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


class HubRead(SQLModel):
    id: int
    name: str
    city: str


class HubCreate(SQLModel):
    name: str
    city: str


class Parcel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tracking_number: str
    weight: float
    hub_id: int = Field(foreign_key='hub.id')
    hub: 'Hub' = Relationship(back_populates='parcels')


class ParcelRead(SQLModel):
    id: int
    tracking_number: str
    weight: float
    hub_id: int


def init_db():
    SQLModel.metadata.create_all(engine)
    print('Database created successfully')


@app.get('/hubs', response_model=list[HubRead])
def read_hubs_data():
    with Session(engine) as session:
        query = select(Hub)
        result = session.exec(query)
        all_hubs = result.all()
        return all_hubs


@app.get('/hubs/{hub_id}', response_model=HubRead)
def read_single_hub(hub_id: int):
    with Session(engine) as session:
        target_hub = session.get(Hub, hub_id)
        if target_hub is None:
            raise HTTPException(status_code=404, detail='Hub not found')
        return target_hub


@app.post('/hubs', response_model=HubRead)
def create_hub_endpoint(hub_in: HubCreate):
    with Session(engine) as session:
        db_hub = Hub(name=hub_in.name, city=hub_in.city)
        session.add(db_hub)
        session.commit()
        session.refresh(db_hub)
        return db_hub


@app.get('/parcels')
def read_parcels_data():
    with Session(engine) as session:
        query = select(Parcel)
        result = session.exec(query)
        all_parcels = result.all()
        return all_parcels


@app.get('/parcels/{parcel_id}')
def read_single_parcel(parcel_id: int):
    with Session(engine) as session:
        target_parcel = session.get(Parcel, parcel_id)
        if target_parcel is None:
            raise HTTPException(status_code=404, detail='Parcel not found')
        return target_parcel


@app.delete('/parcels/{parcel_id}')
def delete_single_parcel(parcel_id: int):
    with Session(engine) as session:
        target_parcel = session.get(Parcel, parcel_id)
        if target_parcel:
            session.delete(target_parcel)
            session.commit()
            return {'status': 'success', 'message': f'Parcel {parcel_id} deleted successfully'}
        else:
            raise HTTPException(status_code=404, detail='Parcel not found')


@app.post('/parcels')
def create_parcel_endpoint(parcel: Parcel):
    with Session(engine) as session:
        session.add(parcel)
        session.commit()
        session.refresh(parcel)
        return parcel


if __name__ == '__main__':
    init_db()