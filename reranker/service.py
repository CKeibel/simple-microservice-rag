from dynaconf import settings
from models.factory import ModelFactory
from models.model import Reranker
from models.schemas import RerankResult


class RankService:
    def __init__(self):
        self.model: Reranker = ModelFactory.get_reranker(settings.MODEL_ID)

    async def rank(self, query: str, docs: list[str]) -> list[RerankResult]:
        return await self.model.rank(query, docs)
