from fastapi import FastAPI, APIRouter
from fastapi import status


app = FastAPI(
    title="Recipe API",
    openapi_url="/openapi.json"
)


appRoute = APIRouter()


app.include_router(appRoute)


@appRoute.get(
    path='/',
    status_code=status.HTTP_200_OK)
async def root() -> dict:
    """_summary_

    Returns:
        dict: _description_
    """
    return {'message': 'Hello World'}
