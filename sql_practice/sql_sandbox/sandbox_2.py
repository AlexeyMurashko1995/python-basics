import asyncio
from decimal import Decimal

from sqlalchemy import Boolean, ForeignKey, Numeric, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    products: Mapped[list["Product"]] = relationship(back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    in_stock: Mapped[bool] = mapped_column(Boolean, default=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="products")
    orders: Mapped[list["Order"]] = relationship(back_populates="product")


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(default=1)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))

    product: Mapped["Product"] = relationship(back_populates="orders")


async def seed_data(session: AsyncSession):
    c_tech = Category(name="Electronics")
    c_books = Category(name="Books")
    c_home = Category(name="Home")

    p1 = Product(title="Smartphone", price=Decimal("800.00"), in_stock=True, category=c_tech)
    p2 = Product(title="Laptop", price=Decimal("1500.00"), in_stock=True, category=c_tech)
    p3 = Product(title="Python Course Book", price=Decimal("50.00"), in_stock=True, category=c_books)
    p4 = Product(title="SQL Guide", price=Decimal("40.00"), in_stock=False, category=c_books)
    p5 = Product(title="Coffee Maker", price=Decimal("150.00"), in_stock=True, category=c_home)

    o1 = Order(quantity=2, total_amount=Decimal("1600.00"), product=p1)
    o2 = Order(quantity=1, total_amount=Decimal("1500.00"), product=p2)
    o3 = Order(quantity=5, total_amount=Decimal("250.00"), product=p3)
    o4 = Order(quantity=1, total_amount=Decimal("800.00"), product=p1)
    o5 = Order(quantity=3, total_amount=Decimal("450.00"), product=p5)

    session.add_all([c_tech, c_books, c_home, p1, p2, p3, p4, p5, o1, o2, o3, o4, o5])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        # query = select(Product.title, Product.price).where(Product.in_stock==True, Product.price < 100)
        # query = select(Product.title, Category.name).join(Category).where(Product.in_stock==False)
        # query = select(Product.title, func.sum(Order.total_amount)).join(Order).group_by(Product.title)
        # query = (
        # select(Category.name, func.sum(Order.quantity))
        # .select_from(Category)
        # .join(Product).join(Order)
        # .group_by(Category.name).
        # having(func.sum(Order.quantity) > 2)
        # )
        query = select(Category.name, func.avg(Product.price).label("avg_price")).join(Product).group_by(Category.name)

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())