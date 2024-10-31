from abc import ABC, abstractmethod

import torch
from models.schemas import RerankResult
from sentence_transformers import CrossEncoder, SentenceTransformer


class Reranker(ABC):
    def __init__(self, model_id: str) -> None:
        pass

    @abstractmethod
    def rerank(self, query: str, docs: list[str]) -> list[RerankResult]:
        pass


class CrossEncoderWrapper(Reranker):
    def __init__(self, model_id: str) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = CrossEncoder(model_id, device=self.device)

    def rerank(self, query: str, docs: list[str]) -> list[RerankResult]:
        result = self.model.rank(query, docs)
        return [RerankResult(**r) for r in result]


class SentenceTransformerWrapper(Reranker):
    def __init__(self, model_id: str) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(model_id, device=self.device)

    def rerank(self, query: str, docs: list[str]) -> list[RerankResult]:
        e_query = self.model.encode(query)
        e_docs = self.model.encode(docs)
        results = self.model.similarity(e_query, e_docs)[0].tolist()
        return [
            RerankResult(corpus_id=i, score=score, text=text)
            for i, (score, text) in enumerate(results, docs)
        ]
