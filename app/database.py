import logging
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.my_app.models import User  # import models inheriting from beanie.Document

from app.settings import settings

DOCUMENT_MODELS = [User]  # include all models inheriting from beanie.Document


async def init_db(
    db_address: str = settings.db_address, db_name: str = settings.db_name
):
    try:
        client = AsyncIOMotorClient(db_address)
        db = client.get_database(db_name)
        await init_beanie(database=db, document_models=DOCUMENT_MODELS)
        logging.info(
            "✅ Database initialized successfully.", "\n", f"db_name: {db_name}"
        )
    except Exception as e:
        logging.exception("❌ Failed to initialize database.")
        raise e
