import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession

from DataBase.models import User
from DataBase.schemas import UserDTO


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_user_by_id(self, user_id: int) -> UserDTO | None:
        query = sqlalchemy.select(User).where(User.user_id == user_id)
        scalar: User | None = await self._session.scalar(query)
        return UserDTO.model_validate(scalar) if scalar is not None else None

    async def save_new_user(self, user_id: int) -> None:
        user = User(user_id=user_id)
        self._session.add(user)
        await self._session.flush()

    async def update_user(self, user_id: int, **kwargs) -> None:
        query = sqlalchemy.update(User).where(User.user_id == user_id).values(**kwargs)
        await self._session.execute(query)
        await self._session.flush()

    async def get_user_by_email(self, email: str) -> UserDTO | None:
        query = sqlalchemy.select(User).where(User.email == email)
        scalar: User | None = await self._session.scalar(query)
        return UserDTO.model_validate(scalar) if scalar is not None else None
