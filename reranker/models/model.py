from abc import ABC, abstractmethod

import torch
from models.schemas import RerankResult
from sentence_transformers import CrossEncoder, SentenceTransformer


class Reranker(ABC):
    def __init__(self, model_id: str) -> None:
        pass

    @abstractmethod
    async def rank(self, query: str, docs: list[str]) -> list[RerankResult]:
        pass


class CrossEncoderWrapper(Reranker):
    def __init__(self, model_id: str) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = CrossEncoder(model_id, device=self.device)

    async def rank(self, query: str, docs: list[str]) -> list[RerankResult]:
        result = self.model.rank(query, docs)
        return [
            RerankResult(
                score=r["score"], corpus_id=r["corpus_id"], text=docs[r["corpus_id"]]
            )
            for r in result
        ]


class BiEncoderWrapper(Reranker):
    def __init__(self, model_id: str) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(model_id, device=self.device)

    async def rank(self, query: str, docs: list[str]) -> list[RerankResult]:
        e_query = self.model.encode(query)
        e_docs = self.model.encode(docs)
        results = self.model.similarity(e_query, e_docs)[0].tolist()
        results = [
            RerankResult(corpus_id=i, score=score, text=text)
            for i, (score, text) in enumerate(results, docs)
        ]
        return sorted(results, key=lambda x: x.score, reverse=True)
