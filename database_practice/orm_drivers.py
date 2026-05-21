from sqlmodel import SQLModel, Field, Session, create_engine

class Driver(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    car_model: str
    is_active: bool

sql_file_name = 'database.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)

if __name__=='__main__':

    driver_one = Driver(name='Ivan', car_model='Scania', is_active=True)
    driver_two = Driver(name='Egor', car_model='Volvo', is_active=False)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(driver_one)
        session.add(driver_two)

        session.commit()

