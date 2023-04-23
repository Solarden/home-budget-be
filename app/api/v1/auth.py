from typing import Annotated, Union

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
def read_root():
    """Root endpoint."""
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):  # pylint: disable=invalid-name
    """Item endpoint."""
    return {"item_id": item_id, "q": q}


@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    """Items endpoint."""
    return {"token": token}
