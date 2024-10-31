from models.schemas import RerankResult
from pydantic import BaseModel, Field


class RankRequest(BaseModel):
    query: str = Field(
        example="What is the capital of France?", title="The query to rank against"
    )
    docs: list[str] = Field(
        example=[
            "Germany won the world cup",
            "Italian pizza is delicious",
            "Paris is the captial of france",
            "I love spending vacation in spain.",
        ],
        title="The corpus to rank against",
    )


class RankResponse(BaseModel):
    results: list[RerankResult]
