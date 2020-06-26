import pymongo
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from nltk import tokenize
from typing import List

from slugify import slugify

from .article_model import ArticleInDB, ArticleBase, FilterParams
from .config import database_name, article_collection_name, sentences_collection_name
from .sentence_model import SentenceInDB, Sentence
from .text_utils import preprocess


async def get_article_by_slug(
        conn: AsyncIOMotorClient, slug: str
) -> ArticleInDB:
    article_doc = await _get_collection(conn, article_collection_name).find_one({"slug": slug})
    if article_doc:
        return ArticleInDB(**article_doc, created_at=ObjectId(article_doc["_id"]).generation_time)


async def create_sentences(conn: AsyncIOMotorClient, body: str, slug: str) -> List[Sentence]:
    sentences = []
    for sentence in tokenize.sent_tokenize(body):
        sentence_dict = {
            'sentence_original': sentence,
            'sentence_processes': preprocess(sentence),
            'slug': slug
        }
        await _get_collection(conn, sentences_collection_name).insert_one(sentence_dict)
        sentences.append(Sentence(**sentence_dict))
    return sentences


async def create_article_by_slug(
        conn: AsyncIOMotorClient, article: ArticleBase, sentences: list
) -> ArticleInDB:
    slug = slugify(article.title)

    article_doc = article.dict()
    article_doc["slug"] = slug
    article_doc["sentence_list"] = [sentence.sentence_original for sentence in sentences]
    await _get_collection(conn, article_collection_name).insert_one(article_doc)
    return ArticleInDB(**article_doc, created_at=ObjectId(article_doc["_id"]).generation_time)


async def fetch_all_sentences(conn: AsyncIOMotorClient) -> List[SentenceInDB]:
    sentences = []
    rows = _get_collection(conn, sentences_collection_name).find()
    async for row in rows:
        sentences.append(SentenceInDB(**row))
    return sentences


async def fetch_all_articles(conn: AsyncIOMotorClient, filters: FilterParams) -> List[ArticleInDB]:
    articles = []
    rows = _get_collection(conn, article_collection_name).find(limit=filters.limit).sort(
        "_id", pymongo.DESCENDING
    )
    async for row in rows:
        articles.append(ArticleInDB(**row, created_at=ObjectId(row["_id"]).generation_time))
    return articles


def _get_collection(conn, collection_name):
    return conn[database_name][collection_name]
