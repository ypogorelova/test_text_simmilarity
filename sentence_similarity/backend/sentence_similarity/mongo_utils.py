import logging

from motor.motor_asyncio import AsyncIOMotorClient

from sentence_similarity.backend.sentence_similarity.config import MONGODB_URL
from sentence_similarity.backend.sentence_similarity.db import db


async def connect_to_mongo():
    logging.info("Connecting to Mongo...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL))
    logging.info("Connected")


async def close_mongo_connection():
    logging.info("Closing connection to Mongo...")
    db.client.close()
    logging.info("Shutdown Mongo")
