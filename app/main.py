from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.database import init_db
from app.my_app.controllers import (
    router,
)  # import routers; they must be of type: fastapi.APIRouter
from app.settings import settings
import logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("🔌 Initializing DB connection...")
    await init_db(settings.db_address, settings.db_name)

    yield

    logging.info("🛑 Cleaning up on shutdown...")
    if hasattr(app.state, "listener"):
        app.state.listener.cancel()


def create_app() -> FastAPI:
    """Factory function to create a FastAPI app instance."""
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
    )

    # incluide routers here; they must be of type: fastapi.APIRouter
    app.include_router(router)

    @app.get("/")
    async def get_health():
        return JSONResponse(status_code=200, content={"message": "Server is running."})

    return app


app = create_app()
