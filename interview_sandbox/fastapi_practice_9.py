import asyncio
from typing import List
from sqlalchemy import ForeignKey, String, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload

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


async def get_author_selectinload(author_id: int, session: AsyncSession) -> Author:
    query = (
        select(Author)
        .options(selectinload(Author.books))
        .where(Author.id==author_id)
    )
    result = await session.execute(query)
    return result.scalar_one()


async def main():
    await init_db()

    async with async_session() as session:
        author = await get_author_selectinload(1, session)
        print(f"Author:{author.name}")
        print(f"Books: {[book.title for book in author.books]}")


if __name__ == "__main__":
    asyncio.run(main())