from sentence_transformers import SentenceTransformer

from sentense_similarity.backend.db_operations import fetch_all_sentences
from sentense_similarity.backend.db import get_database


class TextManager(object):
    instance = None

    @classmethod
    async def create(cls):
        self = TextManager()
        self.embedder = SentenceTransformer('bert-base-nli-mean-tokens')
        self.original_sentences = await fetch_all_sentences(await get_database())
        return self

    @classmethod
    async def get_instance(cls):
        if cls.instance is None:
            cls.instance = await cls.create()
        return cls.instance

    def add_new_sentences(self, more_sentences):
        self.original_sentences.extend(more_sentences)

    async def get_clean_sentences(self):
        sentences = self.original_sentences
        return [sentence.sentence_processes for sentence in sentences]

    @property
    async def corpus_embeddings(self):
        corpus = await self.get_clean_sentences()
        return self.embedder.encode(corpus)
