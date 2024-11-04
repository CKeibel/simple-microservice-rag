from pydantic import BaseModel, Field


class Document(BaseModel):
    id: str
    text: str
    metadata: dict = Field(default_factory=dict)


class IntermediateResult(BaseModel):
    queries: list[str]
    query_vectors: list[list[float]] | None = None
    documents: list[list[Document]] = Field(default_factory=list)
    outputs: list[str] | None = None
