from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


async def database_connection_init(db_url: str) -> async_sessionmaker[AsyncSession]:
    """
    Иницализация подключения к базе данных.

    :param db_url: Строка подключения к базе данных.
    :return: Асинхронный делатель сессий. :)
    """
    async_engine = create_async_engine(db_url)

    # Проверка подключения к базе данных
    async with async_engine.begin():
        pass

    return async_sessionmaker(
        bind=async_engine,
        autoflush=False,
        future=True,
        expire_on_commit=False,
    )
