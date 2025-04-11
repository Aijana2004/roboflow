from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config import config
from models import PredictionModel


client = AsyncIOMotorClient(
    config.MONGODB_URL
)
db = client[config.DB_NAME]


async def init_db():
    await init_beanie(database=db,document_models=[PredictionModel])

try:
    client.server_info()
    print('база данныхка уланды')
except Exception as e:
    print(f'ошибка {e}')