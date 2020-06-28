from typing import List

from pydantic import Schema

from .db_model import DateTimeModelMixin, DBModelMixin
from sentence_similarity.backend.sentence_similarity.rw_model import RWModel


class ArticleFilterParams(RWModel):
    limit: int = 20
    offset: int = 0


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


class ArticleInCreate(ArticleBase):
    pass
