import logging

from motor.motor_asyncio import AsyncIOMotorClient

from sentense_similarity.backend.config import MONGODB_URL
from sentense_similarity.backend.db import db


async def connect_to_mongo():
    logging.info("Connecting to Mongo...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL))
    logging.info("Connected")


async def close_mongo_connection():
    logging.info("Closing connection to Mongo...")
    db.client.close()
    logging.info("Shutdown Mongo")
