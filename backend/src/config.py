import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URI = os.environ.get("DATABASE_URI")
    JWT_SECRET = os.environ.get("JWT_SECRET")

root_dir = os.path.dirname(__file__)