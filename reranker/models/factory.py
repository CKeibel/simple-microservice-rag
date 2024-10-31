import sys

from models.model import CrossEncoderWrapper, Reranker, SentenceTransformerWrapper


class RerenakerFactory:
    @staticmethod
    def get_reranker(model_id: str) -> Reranker:
        model = None
        try:
            model = CrossEncoderWrapper(model_id)
            return model
        except Exception:
            try:
                model = SentenceTransformerWrapper(model_id)
                return model
            except Exception:
                sys.exit(1)
