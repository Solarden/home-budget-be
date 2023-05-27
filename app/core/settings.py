from decouple import config

# App general settings
PROJECT_NAME = config("PROJECT_NAME", default="Home Budget API")
DEBUG = config("DEBUG", cast=bool, default=False)

# Database settings
DATABASE_URL = config("DATABASE_URL")
SQLALCHEMY_POOL_SIZE = config("SQLALCHEMY_POOL_SIZE", cast=int, default=20)
SQLALCHEMY_MAX_OVERFLOW = config("SQLALCHEMY_MAX_OVERFLOW", cast=int, default=80)
SQLALCHEMY_POOL_TIMEOUT = config("SQLALCHEMY_POOL_TIMEOUT", cast=int, default=10)

# OAuth2 settings
SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)
