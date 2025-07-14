import ssl
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession  # ✅ use sqlmodel AsyncSession
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
)
from sqlalchemy.orm import sessionmaker

from src.config import Config
from src.books.models import Book  # if needed to import your models

# 📄 Create SSL context for secure connection
ssl_context = ssl.create_default_context()

# 📄 Create Async Engine
engine: AsyncEngine = create_async_engine(
    Config.DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context}  # pass SSL context explicitly
)


async def initdb() -> None:
    """
    Initialize the database and create all tables
    """
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# 📄 Create sessionmaker once
async_sessionmaker = sessionmaker(
    bind=engine,
    class_=AsyncSession,  # ✅ use sqlmodel.ext.asyncio.session.AsyncSession
    expire_on_commit=False
)


async def get_session():
    """
    Dependency to provide an AsyncSession
    """
    async with async_sessionmaker() as session:
        yield session
