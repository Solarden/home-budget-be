from typing import Union

from fastapi import FastAPI

from app.core import settings

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)


@app.get("/")
def read_root():
    """Root endpoint."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):  # pylint: disable=invalid-name
    """Item endpoint."""
    return {"item_id": item_id, "q": q}
