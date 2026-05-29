from sqlmodel import SQLModel, Field, Session, create_engine, Relationship
from fastapi import FastAPI


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


app = FastAPI()

sql_file_name = 'delivery_service.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)

if __name__ == '__main__':
    init_db()