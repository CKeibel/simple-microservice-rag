import chromadb
from database_conectors.base import DatabaseConnector
from schemas import Document


class ChromaDBConnector(DatabaseConnector):
    def __init__(self, host: str, port: int, **kwargs):
        super().__init__(host, port, **kwargs)
        self.client = chromadb.HttpClient(host=self.host, port=self.port)

    def create_collection(self, collection_name: str) -> None:
        pass

    def get_collection_names(self) -> list[str]:
        pass

    def insert(self, documents: Document | list[Document]) -> None:
        pass

    def query(self, query: list[list[float]]) -> list[Document]:
        pass
