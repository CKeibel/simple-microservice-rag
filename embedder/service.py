from dynaconf import settings
from model import SBERTWrapper
from schemas import EmbeddingResponse


class EmbeddingService:
    def __init__(self) -> None:
        self.model = SBERTWrapper(settings.MODEL_ID)

    async def embed(self, text: str | list[str]) -> EmbeddingResponse:
        return await self.model.embed(text)
