from pydantic import BaseModel


class RerankResult(BaseModel):
    corpus_id: str
    score: float
    text: str
