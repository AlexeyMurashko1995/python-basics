from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    price: Mapped[float]