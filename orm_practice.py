from sqlmodel import Field, SQLModel

class Cargo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_tracking: str
    destination: str
    weight: int
    status: str