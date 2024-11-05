from abc import ABC, abstractmethod

from schemas import Document


class DatabaseConnector(ABC):
    def __init__(self, host: str, port: int, **kwargs):
        self.host = host
        self.port = port
        self.kwargs = kwargs

    @abstractmethod
    def create_collection(self, collection_name: str) -> None:
        pass

    @abstractmethod
    def get_collection_names(self) -> list[str]:
        pass

    @abstractmethod
    def insert(self, documents: Document | list[Document]) -> None:
        pass

    @abstractmethod
    def query(self, query: list[list[float]]) -> list[Document]:
        pass
