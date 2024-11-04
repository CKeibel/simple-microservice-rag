from pydantic import BaseModel


class RerankResult(BaseModel):
    corpus_id: int
    score: float
    text: str


class RankResponse(BaseModel):
    results: list[RerankResult]
