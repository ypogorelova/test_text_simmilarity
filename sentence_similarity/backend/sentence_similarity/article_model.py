from typing import List

from pydantic import Schema

from .db_model import DateTimeModelMixin, DBModelMixin, RWModel


class FilterParams(RWModel):
    limit: int = 100


class ArticleBase(RWModel):
    title: str
    body: str


class Article(DateTimeModelMixin, ArticleBase):
    slug: str
    sentence_list: List[str] = Schema([], alias="sentenceList")


class ArticleInDB(DBModelMixin, Article):
    pass


class ArticleInResponse(RWModel):
    article: Article


class ManyArticlesInResponse(RWModel):
    articles: List[Article]
    articles_count: int = Schema(..., alias="articlesCount")
