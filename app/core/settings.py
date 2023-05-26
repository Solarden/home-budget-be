from decouple import config

PROJECT_NAME = config("PROJECT_NAME", default="Home Budget API")
DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URL = config("DATABASE_URL")
