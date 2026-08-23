import asyncio

from sqlalchemy import ForeignKey, Integer, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    tasks: Mapped[list["Task"]] = relationship(back_populates="project")


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    hours_spent: Mapped[int] = mapped_column(Integer)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))

    project: Mapped["Project"] = relationship(back_populates="tasks")


async def seed_data(session: AsyncSession):
    p_backend = Project(name="Backend Development")
    p_mobile = Project(name="Mobile App")
    p_devops = Project(name="DevOps Setup")

    t1 = Task(title="Database Schema Design", hours_spent=10, project=p_backend)
    t2 = Task(title="API Auth Endpoint", hours_spent=25, project=p_backend)
    t3 = Task(title="ORM Optimization", hours_spent=40, project=p_backend)

    t4 = Task(title="UI Login Screen", hours_spent=5, project=p_mobile)
    t5 = Task(title="Push Notifications", hours_spent=15, project=p_mobile)

    t6 = Task(title="Docker Setup", hours_spent=12, project=p_devops)
    t7 = Task(title="CI/CD Pipeline", hours_spent=33, project=p_devops)

    session.add_all([p_backend, p_mobile, p_devops, t1, t2, t3, t4, t5, t6, t7])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        avg_time = select(func.avg(Task.hours_spent)).scalar_subquery()
        query = select(Task.title, Task.hours_spent).where(Task.hours_spent > avg_time)

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())