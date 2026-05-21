from sqlmodel import Field, SQLModel, create_engine



class Cargo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_tracking: str
    destination: str
    weight: int
    status: str

cargo_one = Cargo(
    id_tracking='TRK-101', destination='Warsaw', weight=450, status='In Transit'
)

cargo_two = Cargo(
    id_tracking='TRK-202', destination='Wroclaw', weight=890, status='Delivered'
)

print(f'Cargo {cargo_one.id_tracking} has weight {cargo_one.weight} kg')
print(f'Cargo {cargo_two.id_tracking} has weight {cargo_two.weight} kg')

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url)

SQLModel.metadata.create_all(engine)