from sqlmodel import SQLModel, Field, create_engine, Session, select

class Warehouse(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    city: str
    capacity_tons: int

sql_file_name = 'database.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)

if __name__ == '__main__':

    warehouse_one = Warehouse(name='Janki', city='Warsaw', capacity_tons=550)
    warehouse_two = Warehouse(name='Gdanski', city='Gdansk', capacity_tons=1100)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(warehouse_one)
        session.add(warehouse_two)

        session.commit()

        second_warehouse = session.get(Warehouse, 2)
        if second_warehouse:
            second_warehouse.capacity_tons = 1200
            session.commit()

        first_warehouse = session.get(Warehouse, 1)
        if first_warehouse:
            session.delete(first_warehouse)
            session.commit()

        query = select(Warehouse)
        result = session.exec(query)

        for warehouse in result:
            print(f'Name: {warehouse.name}; City: {warehouse.city}; Capacity tons: {warehouse.capacity_tons}')


