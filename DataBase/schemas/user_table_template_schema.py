from DataBase.schemas.base import BaseDTO


class UserDTO(BaseDTO):
    id: int
    user_id: int
    name: str | None
    email: str | None
    password: str | None
