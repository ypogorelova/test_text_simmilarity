from fastapi import APIRouter, Body, Depends, Path, Query
from motor.motor_asyncio import AsyncIOMotorClient
from slugify import slugify
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_404_NOT_FOUND

from sentense_similarity.backend.db_operations import (
    get_article_by_slug, create_article_by_slug, create_sentences, fetch_all_articles
)
from sentense_similarity.backend.web_utils import create_aliased_response
from sentense_similarity.backend.article_model import (
    ManyArticlesInResponse, ArticleInResponse, ArticleInCreate
)
from sentense_similarity.backend.db import get_database
from sentense_similarity.backend.sentence_model import (
    SentenceList, ManySentenceSimilarityInResponse,
    Sentence)
from sentense_similarity.backend.text_manager import TextManager
from sentense_similarity.backend.text_utils import (
    get_similar_sentences, get_original_sentences_w_scores
)

router = APIRouter()


@router.get("/articles", response_model=ManyArticlesInResponse, tags=["articles"])
async def get_articles(
        db: AsyncIOMotorClient = Depends(get_database),
):
    dbarticles = await fetch_all_articles(db)
    return create_aliased_response(
        ManyArticlesInResponse(articles=dbarticles, articles_count=len(dbarticles))
    )


@router.get("/articles/{slug}", response_model=ArticleInResponse, tags=["articles"])
async def get_article(
        slug: str = Path(..., min_length=1),
        db: AsyncIOMotorClient = Depends(get_database),
):
    dbarticle = await get_article_by_slug(db, slug)
    if not dbarticle:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Article with slug '{slug}' not found",
        )
    return create_aliased_response(
        ArticleInResponse(article=dbarticle)
    )


@router.post(
    "/articles",
    response_model=ArticleInResponse,
    tags=["articles"],
    status_code=HTTP_201_CREATED,
)
async def create_new_article(
        article: ArticleInCreate = Body(..., embed=True),
        db: AsyncIOMotorClient = Depends(get_database),
):
    article_by_slug = await get_article_by_slug(
        db, slugify(article.title)
    )
    if article_by_slug:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"This article is already exists slug='{article_by_slug.slug}'",
        )
    sentences = await create_sentences(db, article.body, slugify(article.title))
    text_manager = await TextManager.get_instance()
    text_manager.add_new_sentences(sentences)
    dbarticle = await create_article_by_slug(db, article, sentences)
    return create_aliased_response(ArticleInResponse(article=dbarticle))


@router.post("/similar", response_model=SentenceList, tags=["sentences"])
async def get_similar(sentence: str = Body(..., embed=True)):
    text_manager = await TextManager.get_instance()
    embeddings = await text_manager.corpus_embeddings
    clean_sentences = await text_manager.get_clean_sentences()
    original_sentences = text_manager.original_sentences
    result = get_similar_sentences(clean_sentences, sentence, embeddings, text_manager.embedder)
    if not result:
        return create_aliased_response(
            ManySentenceSimilarityInResponse(sentences=[], sentences_count=len(result))
        )
    else:
        result = get_original_sentences_w_scores(original_sentences, result)
    return create_aliased_response(
        ManySentenceSimilarityInResponse(sentences=result, sentences_count=len(result))
    )
