from core.db import Base

from sqlalchemy.orm import Mapped, mapped_column


class Home(Base):
    __tablename__ = "home"

    id: Mapped[str] = mapped_column(primary_key=True)
