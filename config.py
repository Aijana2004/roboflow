from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    ROBOFLOW_URL = os.getenv("ROBOFLOW_URL")
    MONGODB_URL = os.getenv("MONGODB_URL")
    DB_NAME = os.getenv("DB_NAME")


config = Config()