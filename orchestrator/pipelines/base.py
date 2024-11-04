from abc import ABC, abstractmethod

from schemas import IntermediateResult
from tasks.base import BaseTask


class BasePipeline(ABC):
    def __init__(self) -> None:
        self._tasks: list[BaseTask] = []

    def add(self, tasks: BaseTask | list[BaseTask]) -> None:
        if not isinstance(tasks, list):
            tasks = [tasks]
        self._tasks.extend(tasks)

    @abstractmethod
    async def run(self, data: IntermediateResult, **kwargs) -> IntermediateResult:
        pass
