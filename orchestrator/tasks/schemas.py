from pydantic import BaseModel, Field


class Document(BaseModel):
    id: str
    text: str
    metadata: dict = Field(default_factory=dict)


class IntermediateResult(BaseModel):
    queries: list[str]
    documents: list[Document] = Field(default_factory=list)
