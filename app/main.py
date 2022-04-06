from fastapi import FastAPI, APIRouter
from fastapi import status, HTTPException
from typing import Optional


app = FastAPI(
    title="Recipe API",
    openapi_url="/openapi.json"
)


appRoute = APIRouter()


RECIPES = [
    {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "label": "Chicken Paprikash",
        "source": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "label": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]


@appRoute.get(path="/msg/",
              status_code=200,
              deprecated=True)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}


@appRoute.get(
    path='/api/recipe/{id}',
    status_code=status.HTTP_200_OK)
async def getRecipeById(id: int) -> dict:
    """_summary_

    Args:
        id (int): _description_

    Returns:
        dict: _description_
    """
    result = [recipe for recipe in RECIPES if recipe["id"] == id]
    if result != []:
        return result[0]
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get(
    path='/api/recipe',
    status_code=status.HTTP_200_OK
    )
def getByLabel(keyword:Optional[str] = None,
               max_results: Optional[int] = 10,
               ) -> dict:
    """_summary_

    Args:
        label (str): _description_

    Returns:
        dict: _description_
    """
    if not keyword:
        return {"results": RECIPES[: max_results] }
    results  = filter(lambda recipe:keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results":list(results[:max_results])}


app.include_router(appRoute)

