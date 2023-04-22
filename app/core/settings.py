from decouple import Config

env = Config(".env")

PROJECT_NAME = env("PROJECT_NAME", default="Home Budget API")
DEBUG = env("DEBUG", cast=bool, default=False)
DATABASE_URL = env("DATABASE_URL")
