import logging

from motor.motor_asyncio import AsyncIOMotorClient

from .config import MONGODB_URL


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client


async def connect_to_mongo():
    logging.info("Connecting to Mongo...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL))
    logging.info("Connected")


async def close_mongo_connection():
    logging.info("Closing connection to Mongo...")
    db.client.close()
    logging.info("Shutdown Mongo")
