import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    JWT_SECRET = os.environ.get("JWT_SECRET")

root_dir = os.path.dirname(__file__)