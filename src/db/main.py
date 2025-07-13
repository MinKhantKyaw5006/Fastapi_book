import ssl
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import text
from src.config import Config

# Create SSL context for secure connection
ssl_context = ssl.create_default_context()

engine: AsyncEngine = create_async_engine(
    Config.DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context}  # pass SSL context explicitly
)


async def initdb():
    """Create a connection to our db and test a simple query"""
    async with engine.begin() as conn:
        statement = text("select 'Hello World'")
        result = await conn.execute(statement)
        print(result.scalar())  # print the actual string result
