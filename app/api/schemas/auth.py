from typing import Optional

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class NewUser(BaseModel):
    """Schema for creating a new user"""

    username: str
    email: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]


class Token(BaseModel):
    """Schema for token"""

    access_token: str
    token_type: str
