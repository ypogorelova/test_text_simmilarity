from typing import List

from pydantic import Schema

from sentense_similarity.backend.rw_model import RWModel


class Sentence(RWModel):
    sentence_original: str
    sentence_processes: str
    slug: str


class SentenceSilimarity(RWModel):
    sentence_original: str
    similarity_score: float
    slug: str


class ManySentenceSimilarityInResponse(RWModel):
    sentences: List[SentenceSilimarity]
    sentences_count: int = Schema(..., alias="sentencesCount")


class SentenceInDB(Sentence):
    pass


class SentenceList(RWModel):
    sentences: List[SentenceInDB] = []
