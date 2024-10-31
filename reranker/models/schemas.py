from pydantic import BaseModel


class RerankResult(BaseModel):
    corpus_id: int
    score: float
    text: str
