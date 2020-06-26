from fastapi import APIRouter
from sentense_similarity.backend.endpoints import router as article_router

router = APIRouter()
router.include_router(article_router)