import asyncio
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = "departments"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    employees: Mapped[list["Employee"]] = relationship(back_populates="department")


class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    salary: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))

    department: Mapped["Department"] = relationship(back_populates="employees")


async def seed_data(session: AsyncSession):
    d_it = Department(name="IT")
    d_hr = Department(name="HR")
    d_sales = Department(name="Sales")

    e1 = Employee(name="Alice", salary=Decimal("3000.00"), department=d_it)
    e2 = Employee(name="Bob", salary=Decimal("5000.00"), department=d_it)
    e3 = Employee(name="Charlie", salary=Decimal("2000.00"), department=d_hr)
    e4 = Employee(name="David", salary=Decimal("250.00"), department=d_hr)
    e5 = Employee(name="Eve", salary=Decimal("4000.00"), department=d_sales)

    session.add_all([d_it, d_hr, d_sales, e1, e2, e3, e4, e5])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        # avg_salary = select(func.avg(Employee.salary)).scalar_subquery()
        # query = select(Employee.name, Employee.salary).where(Employee.salary > avg_salary)
        subq = select(Employee.department_id, func.max(Employee.salary).label("max_salary")).group_by(Employee.department_id).subquery()
        query = (
            select(Employee.name, Employee.salary)
            .join(
                subq,
                (Employee.department_id == subq.c.department_id) &
                (Employee.salary == subq.c.max_salary)
            )
        )
        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())