from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload, joinedload
from sqlalchemy import ForeignKey, select
from fastapi import Depends

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped[Author] = relationship(back_populates="books")


async def get_db():
    async with async_session_factory() as session:
        yield session


async def get_author_with_books(author_id: int, session: AsyncSession):
    query = select(Author).where(Author.id==author_id).options(selectinload(Author.books))
    result = await session.execute(query)
    final = result.scalar_one_or_none()
    return final


async def get_books_with_authors(session: AsyncSession) -> list[Book]:
    query = select(Book).options(joinedload(Book.author))
    result = await session.execute(query)
    return result.scalars().all()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with async_session_factory() as session:
        author_1 = Author(name="Alex")
        author_2 = Author(name="Ivan")
        author_3 = Author(name="Oleg")
        book_1 = Book(title="Book_1", author=author_1)
        book_2 = Book(title="Book_2", author=author_2)
        book_3 = Book(title="Book_3", author=author_3)
        session.add_all([author_1, author_2, author_3, book_1, book_2, book_3])
        await session.commit()


async def main():
    start = await init_db()
    async with async_session_factory() as session:
        author = await get_author_with_books(1, session=session)
        if author:
            print(f"Author: {author.name}")
            for book in author.books:
                print(f"Book: {book.title}")

        books = await get_books_with_authors(session=session)
        for book in books:
            print(f" Book: {book.title} | Author: {book.author.name}")


if __name__== "__main__":
    import asyncio
    asyncio.run(main())

