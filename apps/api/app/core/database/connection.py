from sqlalchemy.ext.asyncio import create_async_engine

from app.core.config.settings import APP_SETTINGS

async_engine = create_async_engine(
    url=APP_SETTINGS.switch_db_using_env,
    echo=APP_SETTINGS.DATABASE_ECHO_LOGS,
    future=True,
)
