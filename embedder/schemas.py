from pydantic import BaseModel, Field


class EmbeddingRequest(BaseModel):
    text: str | list[str] = Field(example=["Hello, World!", "Goodbye, World!"])


class EmbeddingResponse(BaseModel):
    embeddings: list[list[float]]
