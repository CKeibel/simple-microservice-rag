from abc import ABC, abstractmethod

import torch
from schemas import EmbeddingResponse
from sentence_transformers import SentenceTransformer


class Embedder(ABC):
    @abstractmethod
    def embed(self, text: str | list[str]) -> EmbeddingResponse:
        pass


class SBERTWrapper(Embedder):
    def __init__(self, model_id: str):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(
            model_id, device=self.device, trust_remote_code=True
        )

    async def embed(self, text: str | list[str]) -> EmbeddingResponse:
        if isinstance(text, str):
            text = [text]
        embeddings = self.model.encode(text).tolist()
        return EmbeddingResponse(embeddings=embeddings)
