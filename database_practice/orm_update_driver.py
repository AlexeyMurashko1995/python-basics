from sqlmodel import Session, create_engine
from orm_drivers import Driver

sql_file_name = 'database.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)

with Session(engine) as session:
    first_driver = session.get(Driver, 1)
    if first_driver:
        first_driver.is_active = False
        session.commit()