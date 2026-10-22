from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from dotenv import load_dotenv
from app.core.settings import settings
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=10,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,

)

class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

