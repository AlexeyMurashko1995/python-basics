from sqlmodel import SQLModel, Field, Session, create_engine, Relationship

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

