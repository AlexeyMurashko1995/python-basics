import asyncio

from sqlalchemy import ForeignKey, Integer, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))

    students: Mapped[list["Student"]] = relationship(back_populates="course")


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    score: Mapped[int] = mapped_column(Integer)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))

    course: Mapped["Course"] = relationship(back_populates="students")


async def seed_data(session: AsyncSession):
    c_python = Course(title="Python Developer")
    c_ds = Course(title="Data Science")
    c_qa = Course(title="QA Automation")

    s1 = Student(name="Alex", score=85, course=c_python)
    s2 = Student(name="Max", score=95, course=c_python)
    s3 = Student(name="Olga", score=60, course=c_python)

    s4 = Student(name="Elena", score=90, course=c_ds)
    s5 = Student(name="Ivan", score=70, course=c_ds)

    s6 = Student(name="Dmitriy", score=50, course=c_qa)
    s7 = Student(name="Anna", score=80, course=c_qa)

    session.add_all([c_python, c_ds, c_qa, s1, s2, s3, s4, s5, s6, s7])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        avg_score = select(func.avg(Student.score).label("avg_score")).scalar_subquery()
        query = (
            select(Student.name, Student.score)
            .where(Student.score > avg_score)
        )

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())