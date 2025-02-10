from functools import cached_property
from urllib import parse

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .constant import PROJECT_DIR_PATH

parse_settings = SettingsConfigDict(
    env_file=PROJECT_DIR_PATH / ".env",
    env_file_encoding="utf-8",
    extra="ignore",
)

class DBConfig(BaseSettings):
    model_config = parse_settings

    db_host: str = Field()
    db_port: int = Field()
    db_name: str = Field()
    db_user: str = Field()
    db_password: str = Field()

    def build_postgresql_url(self) -> str:
        """
        Формирует URL для подключения к PostgreSQL.

        :param dbname: Название базы данных
        :param user: Имя пользователя
        :param password: Пароль
        :param host: Хост (по умолчанию 'localhost')
        :param port: Порт (по умолчанию '5432')
        :return: Строка подключения в формате URL
        """
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


def get_db_config() -> DBConfig:
    return DBConfig()