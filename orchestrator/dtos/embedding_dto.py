from pydantic import BaseModel


class EmbeddingResponse(BaseModel):
    embeddings: list[list[float]]
