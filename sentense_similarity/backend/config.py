import os

from dotenv import load_dotenv
from databases import DatabaseURL

API_STR = "/api"

load_dotenv(".env")

MONGODB_URL = os.getenv("MONGODB_URL", "")  # deploying without docker-compose
if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_DB = os.getenv("MONGO_DB", "fastapi")

    MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)

database_name = MONGO_DB
article_collection_name = "articles"
sentences_collection_name = "sentences"
closest_n = 1000
