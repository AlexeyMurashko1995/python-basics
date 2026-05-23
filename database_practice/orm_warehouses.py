from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship

class Cargo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    weight_tons: int
    warehouse_id: int = Field(foreign_key='warehouse.id')
    warehouse: 'Warehouse' = Relationship(back_populates='cargos')

class Warehouse(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    city: str
    capacity_tons: int
    cargos: list['Cargo'] = Relationship(back_populates='warehouse')

sql_file_name = 'database.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)


def init_db_and_add_warehouses():
    warehouse_one = Warehouse(name='Janki', city='Warsaw', capacity_tons=550)
    warehouse_two = Warehouse(name='Gdanski', city='Gdansk', capacity_tons=1100)

    cargo_one = Cargo(name='Electronics', weight_tons=50, warehouse_id=1)
    cargo_two = Cargo(name='Apparel', weight_tons=120, warehouse_id=2)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(warehouse_one)
        session.add(warehouse_two)

        session.add(cargo_one)
        session.add(cargo_two)

        session.commit()


def update_warehouse_capacity(warehouse_id: int, new_capacity: int):
    with Session(engine) as session:
        target_warehouse = session.get(Warehouse, warehouse_id)
        if target_warehouse:
            target_warehouse.capacity_tons = new_capacity
            session.commit()


def delete_warehouse(warehouse_id: int):
    with Session(engine) as session:
        target_warehouse = session.get(Warehouse, warehouse_id)
        if target_warehouse:
            session.delete(target_warehouse)
            session.commit()


def show_all_warehouses():
    with Session(engine) as session:
        query = select(Warehouse)
        result = session.exec(query)

        for warehouse in result:
            print(f'Warehouse name: {warehouse.name} is located in {warehouse.city}; capacity tons: {warehouse.capacity_tons}')

            cargo_query = select(Cargo).where(Cargo.warehouse_id == warehouse.id)
            cargos = session.exec(cargo_query)
            for cargo in cargos:
                print(f'Cargo: {cargo.name}; weight - {cargo.weight_tons} t')


if __name__ == '__main__':
    init_db_and_add_warehouses()
    update_warehouse_capacity(2, 1200)
    # delete_warehouse(1)
    show_all_warehouses()