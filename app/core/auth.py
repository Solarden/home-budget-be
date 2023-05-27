from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import Dict
from typing import Optional

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core import settings
from app.models.user import User


class AuthBase:
    """Base class for authentication."""

    crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


class UserCreator(AuthBase):
    """User creator."""

    def __init__(self, db: Session, user_data: Dict[str, str]):
        self.db = db
        self.username = user_data["username"]
        self.password = user_data["password"]
        self.email = user_data["email"]
        self.first_name = user_data["first_name"]
        self.last_name = user_data["last_name"]

    def _get_password_hash(self) -> str:
        """Get password hash."""
        return self.crypt_context.hash(self.password)

    def create_user(self) -> User:
        """Create user."""
        user: User = User(
            username=self.username,
            email=self.email,
            hashed_password=self._get_password_hash(),
            first_name=self.first_name,
            last_name=self.last_name,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user


class UserAuth(AuthBase):
    """User authentication."""

    @staticmethod
    def create_access_token(data: Dict[str, Any], expires_delta: timedelta) -> str:
        """Create access token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password."""
        return self.crypt_context.verify(plain_password, hashed_password)

    def authenticate_user(self, db: Session, username: str, password: str) -> Optional[User]:
        """Authenticate user."""
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return None
        if not self.verify_password(password, user.hashed_password):
            return None
        return user


user_auth = UserAuth()
