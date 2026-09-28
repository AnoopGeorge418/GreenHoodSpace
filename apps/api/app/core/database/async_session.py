from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.config.settings import APP_SETTINGS
from app.core.database.connection import async_engine

AsyncLocalSession = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autoflush=APP_SETTINGS.DATABASE_AUTO_FLUSH,
    expire_on_commit=APP_SETTINGS.DATABASE_AUTO_COMMIT,
)
