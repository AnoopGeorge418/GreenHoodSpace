"""Entry point for api."""

from fastapi import FastAPI
from uvicorn import run

from app.core.config.settings import APP_SETTINGS
from app.modules.healthz.routes.health_route import health_route

app = FastAPI(
    title=APP_SETTINGS.APP_NAME,
    description=APP_SETTINGS.APP_DESCRIPTION,
    version=APP_SETTINGS.APP_VERSION,
)

# registering routes
app.include_router(
    router=health_route, prefix=f"/{APP_SETTINGS.SERVER_BASE_API}"
)

if __name__ == "__main__":
    run(
        app=APP_SETTINGS.SERVER_PATH,
        host=APP_SETTINGS.SERVER_HOST,
        port=APP_SETTINGS.SERVER_PORT,
        reload=APP_SETTINGS.SERVER_RELOAD,
    )
