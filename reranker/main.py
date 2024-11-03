from fastapi import FastAPI
from schemas import RankRequest, RankResponse
from service import RankService

app = FastAPI()

service = RankService()


@app.post("/rank", response_model=RankResponse)
async def rank(request: RankRequest):
    results = await service.rank(request.query, request.docs)
    return RankResponse(results=results)
