from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncAttrs
)
import os

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "app")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "1234")
POSTGRES_DB = os.getenv("POSTGRES_DB", "app")

from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase, AsyncAttrs):
    
    @property
    def id_dict(self):
        return {"id": self.id}
    
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# SessionDependency = Annotated[AsyncSession, Depends(get_session)]

async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
async def close_orm():
    await engine.dispose()
    
