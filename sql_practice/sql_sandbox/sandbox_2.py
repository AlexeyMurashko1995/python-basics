import asyncio
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, select, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = "departments"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    employees: Mapped[list["Employee"]] = relationship(back_populates="department")


class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    salary: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))

    department: Mapped["Department"] = relationship(back_populates="employees")
    sales: Mapped[list["Sale"]] = relationship(back_populates="employee")


class Sale(Base):
    __tablename__ = "sales"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))

    employee: Mapped["Employee"] = relationship(back_populates="sales")


async def seed_data(session: AsyncSession):
    d_it = Department(name="IT")
    d_sales = Department(name="Sales")

    e1 = Employee(name="Alex", salary=Decimal("3000.00"), department=d_it)
    e2 = Employee(name="Maria", salary=Decimal("4500.00"), department=d_sales)
    e3 = Employee(name="Ivan", salary=Decimal("2500.00"), department=d_sales)

    s1 = Sale(amount=Decimal("500.00"), employee=e2)
    s2 = Sale(amount=Decimal("1500.00"), employee=e2)
    s3 = Sale(amount=Decimal("700.00"), employee=e3)
    s4 = Sale(amount=Decimal("300.00"), employee=e1)

    session.add_all([d_it, d_sales, e1, e2, e3, s1, s2, s3, s4])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        # query = select(Employee.name, Employee.salary).where(Employee.salary > 2800).order_by(Employee.salary.desc())
        # query = select(Employee.name, Employee.salary).where((Employee.id==1) | (Employee.id==3))
        # query = select(func.count(Sale.id))
        # query = select(Employee.name, Department.name).join(Employee.department)
        query = select(Sale.amount, Employee.name).join(Sale.employee)

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())