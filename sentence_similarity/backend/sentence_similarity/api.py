from fastapi import APIRouter
from sentence_similarity.backend.sentence_similarity.endpoints import router as article_router

router = APIRouter()
router.include_router(article_router)
