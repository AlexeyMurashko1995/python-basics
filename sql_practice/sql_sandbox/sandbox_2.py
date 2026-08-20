import asyncio
from datetime import date
from decimal import Decimal

from sqlalchemy import Boolean, Date, ForeignKey, Numeric, String, func, select
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
    budget: Mapped[Decimal] = mapped_column(Numeric(12, 2))

    employees: Mapped[list["Employee"]] = relationship(back_populates="department")


class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    salary: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))

    department: Mapped["Department"] = relationship(back_populates="employees")
    sales: Mapped[list["Sale"]] = relationship(back_populates="employee")


class Sale(Base):
    __tablename__ = "sales"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    category: Mapped[str] = mapped_column(String(50))
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))

    employee: Mapped["Employee"] = relationship(back_populates="sales")


async def seed_data(session: AsyncSession):
    d_it = Department(name="IT", budget=Decimal("100000.00"))
    d_sales = Department(name="Sales", budget=Decimal("150000.00"))
    d_support = Department(name="Support", budget=Decimal("50000.00"))

    e1 = Employee(name="Alex", salary=Decimal("3000.00"), is_active=True, department=d_it)
    e2 = Employee(name="Maria", salary=Decimal("4500.00"), is_active=True, department=d_sales)
    e3 = Employee(name="Ivan", salary=Decimal("2500.00"), is_active=False, department=d_sales)
    e4 = Employee(name="Elena", salary=Decimal("5000.00"), is_active=True, department=d_sales)
    e5 = Employee(name="Petr", salary=Decimal("2000.00"), is_active=True, department=d_support)

    s1 = Sale(amount=Decimal("500.00"), category="Software", employee=e2)
    s2 = Sale(amount=Decimal("1500.00"), category="Hardware", employee=e2)
    s3 = Sale(amount=Decimal("700.00"), category="Software", employee=e3)
    s4 = Sale(amount=Decimal("300.00"), category="Services", employee=e1)
    s5 = Sale(amount=Decimal("2200.00"), category="Hardware", employee=e4)
    s6 = Sale(amount=Decimal("1200.00"), category="Software", employee=e4)
    s7 = Sale(amount=Decimal("400.00"), category="Services", employee=e5)
    s8 = Sale(amount=Decimal("800.00"), category="Services", employee=e2)
    s9 = Sale(amount=Decimal("3000.00"), category="Hardware", employee=e4)

    session.add_all([d_it, d_sales, d_support, e1, e2, e3, e4, e5, s1, s2, s3, s4, s5, s6, s7, s8, s9])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        query = select(func.count(Sale.id).label("total_count"), func.sum(Sale.amount).label("total_amount"))

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())