from fastapi import FastAPI
import routers
from database import init_db
import uvicorn
from contextlib import asynccontextmanager
from routers import animal_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

chek_app = FastAPI()
chek_app.include_router(routers.animal_router)



if __name__ == '__main__':
    uvicorn.run(chek_app, host='127.0.0.1', port=8000, workers=True)