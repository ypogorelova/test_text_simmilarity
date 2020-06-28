import collections
from typing import List

import scipy
from nltk import word_tokenize
from numpy import ndarray
from sentence_transformers import SentenceTransformer
from spacy.lang.en import STOP_WORDS

from sentence_similarity.backend.sentence_similarity.config import closest_n
from sentence_similarity.backend.sentence_similarity.sentence_model import SentenceSilimarity


def preprocess(sentence: str) -> str:
    sentence = sentence.lower()
    sentence = word_tokenize(sentence)
    sentence = [w for w in sentence if not w in STOP_WORDS]
    sentence = [w for w in sentence if w.isalpha()]
    return " ".join([i for i in sentence])


def get_similar_sentences(
        corpus: List[str],
        search: str,
        corpus_embeddings: List[ndarray],
        embedder: SentenceTransformer
) -> dict:
    if not corpus:
        return {}

    query_embeddings = embedder.encode(search)

    distances = scipy.spatial.distance.cdist(query_embeddings, corpus_embeddings, "cosine")[0]

    results = zip(range(len(distances)), distances)
    results = sorted(results, key=lambda x: x[1])

    return {corpus[idx]: 1 - distance for idx, distance in results[0:closest_n]}


def get_original_sentences_w_scores(
        all_sentences: List[str], similar_sentences: dict
) -> List[SentenceSilimarity]:
    sorted_sentences = collections.defaultdict(list)

    for sentence in all_sentences:
        sorted_sentences[sentence.sentence_processes].append(sentence)

    res = []
    for k, v in similar_sentences.items():
        found_sentence = sorted_sentences.get(k)
        if found_sentence:
            for i in found_sentence:
                res.append(
                    SentenceSilimarity(
                        sentence_original=i.sentence_original,
                        similarity_score=v,
                        slug=i.slug
                    )
                )

    return res
