import asyncio
from typing import List
from sqlalchemy import ForeignKey, String, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload, joinedload

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    books: Mapped[List["Book"]] = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship("Author", back_populates="books")


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        author = Author(name="Leo Tolstoy")
        book1 = Book(title="War and Peace", author=author)
        book2 = Book(title="Anna Karenina", author=author)
        session.add_all([author, book1, book2])
        await session.commit()


async def get_book_joinedload(book_id: int, session: AsyncSession) -> Book:
    query = (
        select(Book)
        .options(joinedload(Book.author))
        .where(Book.id==book_id)
    )
    result = await session.execute(query)
    return result.scalar_one()


async def main():
    await init_db()

    async with async_session() as session:
        book = await get_book_joinedload(1, session)
        print(f"Book:{book.title}")
        print(f"Author: {book.author.name}")


if __name__ == "__main__":
    asyncio.run(main())