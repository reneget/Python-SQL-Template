from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import AlchemyBaseModel


class User(AlchemyBaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False,
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True,
    )
    name: Mapped[str | None] = mapped_column(
        String(128),
        default=None,
        nullable=True,
    )
    email: Mapped[str | None] = mapped_column(
        String(128),
        default=None,
        nullable=True,
    )
    password: Mapped[str | None] = mapped_column(
        String(256),
        default=None,
        nullable=True,
    )
