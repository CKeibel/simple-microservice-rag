from fastapi import Depends, FastAPI
from schemas import RankRequest, RankResponse
from service import RankService

app = FastAPI()


@app.post("/rank", response_model=RankResponse)
def rank(request: RankRequest, service=Depends(lambda: RankService())):
    results = service.rank(request.query, request.docs)
    return RankResponse(results=results)
