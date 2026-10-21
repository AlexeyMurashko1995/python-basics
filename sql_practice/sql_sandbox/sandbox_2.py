import asyncio

from sqlalchemy import Float, ForeignKey, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_name: Mapped[str] = mapped_column(String(50))
    currency: Mapped[str] = mapped_column(String(3), default="EUR")

    transactions: Mapped[list["Transaction"]] = relationship(back_populates="account")


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    amount: Mapped[float] = mapped_column(Float)
    tx_type: Mapped[str] = mapped_column(String(20))  # 'deposit', 'withdrawal'
    status: Mapped[str] = mapped_column(String(20))   # 'completed', 'failed'

    account: Mapped["Account"] = relationship(back_populates="transactions")


async def seed_data(session: AsyncSession):
    a1 = Account(owner_name="Alexei", currency="EUR")
    a2 = Account(owner_name="PayTech Merchant", currency="EUR")
    a3 = Account(owner_name="Partner Corp", currency="PLN")

    t1 = Transaction(account=a1, amount=2000.0, tx_type="deposit", status="completed")
    t2 = Transaction(account=a1, amount=350.0, tx_type="withdrawal", status="completed")
    t3 = Transaction(account=a2, amount=5000.0, tx_type="deposit", status="completed")
    t4 = Transaction(account=a2, amount=1200.0, tx_type="deposit", status="failed")
    t5 = Transaction(account=a3, amount=8600.0, tx_type="deposit", status="completed")
    t6 = Transaction(account=a3, amount=400.0, tx_type="withdrawal", status="failed")

    session.add_all([a1, a2, a3, t1, t2, t3, t4, t5, t6])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        # query = select(Account.owner_name, func.sum(Transaction.amount)).join(Transaction).where(Transaction.tx_type=="deposit", Transaction.status=="completed").group_by(Account.owner_name)
        query = select(Account.owner_name, func.count(Transaction.id), func.sum(Transaction.amount)).join(Transaction).where(Transaction.status=="failed").group_by(Account.owner_name)

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())