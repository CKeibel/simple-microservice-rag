from dynaconf import settings
from models.factory import ModelFactory
from models.model import Reranker
from models.schemas import RerankResult


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class RankService(metaclass=SingletonMeta):
    def __init__(self):
        self.model: Reranker = ModelFactory.get_reranker(settings.MODEL_ID)

    def rank(self, query: str, docs: list[str]) -> list[RerankResult]:
        return self.model.rank(query, docs)
