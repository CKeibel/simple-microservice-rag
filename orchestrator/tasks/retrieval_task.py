import asyncio
from enum import StrEnum
from typing import Literal

import requests
from pydantic import BaseModel, ConfigDict
from schemas import IntermediateResult
from tasks.base import BaseTask


class RetrieverTypesEnum(StrEnum):
    DENSE = "dense"
    SPARSE = "sparse"


retriever_type = Literal[RetrieverTypesEnum.DENSE, RetrieverTypesEnum.SPARSE]


class Retriever(BaseModel):
    model_config: dict = ConfigDict(arbitrary_types_allowed=True)
    name: str
    url: str
    type: retriever_type


class RetrievalTask(BaseTask):
    def __init__(self, retriever: list[Retriever], **kwargs) -> None:
        super().__init__(**kwargs)
        self.retriever = retriever

    async def _retrieve(
        self, query: list[str] | list[list[float]], url: str
    ) -> list:  # TODO: Define return type
        response = await requests.post(url, json={"query": query}).json()  # TODO
        return response

    def rrf(self, results: list):  # TODO
        pass

    async def handle(self, data: IntermediateResult, **kwargs) -> IntermediateResult:
        for retriever in self.retriever:
            tasks = []
            if retriever.type == RetrieverTypesEnum.DENSE and data.query_vectors:
                tasks.append(self._retrieve(data.query_vectors, retriever.url))
            elif retriever.type == RetrieverTypesEnum.SPARSE and data.queries:
                tasks.append(self._retrieve(data.queries, retriever.url))

        results = await asyncio.gather(*tasks)
        self.rrf(results)
        # TODO
