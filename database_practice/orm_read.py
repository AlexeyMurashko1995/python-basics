from sqlmodel import SQLModel, Field, create_engine, Session, select
from orm_practice import Cargo

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url)

with Session(engine) as session:
    query = select(Cargo)

    results = session.exec(query)

    for cargo in results:
        print(f'Cargo id: {cargo.id}; id tracking: {cargo.id_tracking}; status: {cargo.status}')