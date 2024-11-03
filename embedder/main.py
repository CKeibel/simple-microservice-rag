from fastapi import FastAPI
from schemas import EmbeddingRequest, EmbeddingResponse
from service import EmbeddingService

app = FastAPI()
service = EmbeddingService()


@app.post("/embed", response_model=EmbeddingResponse)
async def embed(request: EmbeddingRequest):
    return await service.embed(request.text)
