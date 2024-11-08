import sys

from models.model import BiEncoderWrapper, CrossEncoderWrapper, Reranker


class ModelFactory:
    @staticmethod
    def get_reranker(model_id: str) -> Reranker:
        model = None
        try:
            model = CrossEncoderWrapper(model_id)
            return model
        except Exception:
            try:
                model = BiEncoderWrapper(model_id)
                return model
            except Exception:
                sys.exit(1)
