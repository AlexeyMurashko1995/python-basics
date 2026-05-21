from sqlmodel import SQLModel, Session, Field, select, create_engine
from orm_drivers import Driver

sql_file_name = 'database.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)

with Session(engine) as session:
    query = select(Driver)
    results = session.exec(query)

    for driver in results:
        print(f'Name: {driver.name}; car: {driver.car_model}; status: {driver.is_active}')
