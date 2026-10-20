import asyncio

from sqlalchemy import Float, ForeignKey, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(20), default="client")  # 'client', 'merchant', 'admin'

    orders: Mapped[list["Order"]] = relationship(back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    total_amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(20))  # 'paid', 'pending', 'cancelled'
    category: Mapped[str] = mapped_column(String(30))  # 'electronics', 'bikes', 'services'

    user: Mapped["User"] = relationship(back_populates="orders")


async def seed_data(session: AsyncSession):
    u1 = User(username="alex_dev", role="client")
    u2 = User(username="tech_shop", role="merchant")
    u3 = User(username="bike_rental", role="merchant")

    o1 = Order(user=u1, total_amount=150.0, status="paid", category="bikes")
    o2 = Order(user=u1, total_amount=45.0, status="pending", category="services")
    o3 = Order(user=u2, total_amount=500.0, status="paid", category="electronics")
    o4 = Order(user=u2, total_amount=20.0, status="cancelled", category="electronics")
    o5 = Order(user=u3, total_amount=320.0, status="paid", category="bikes")
    o6 = Order(user=u3, total_amount=90.0, status="pending", category="services")

    session.add_all([u1, u2, u3, o1, o2, o3, o4, o5, o6])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        # query = select(User.username, func.sum(Order.total_amount)).join(Order).where(Order.status=="paid").group_by(User.username)
        query = select(Order.category, func.sum(Order.total_amount)).where(Order.status=="paid").group_by(Order.category).having(func.sum(Order.total_amount) > 200)

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())