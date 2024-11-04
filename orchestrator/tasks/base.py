from abc import ABC, abstractmethod

from orchestrator.schemas import IntermediateResult


class BaseTask(ABC):
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs

    @abstractmethod
    async def handle(data: IntermediateResult, **kwargs) -> IntermediateResult:
        pass
