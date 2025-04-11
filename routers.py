from fastapi import APIRouter,File, HTTPException, UploadFile
from predict import get_prediction


animal_router = APIRouter(prefix='/api',tags=['ChekAnimal'])


@animal_router.post('/predict')
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        if not image_bytes:
            raise HTTPException(status_code=400,  detail='файл туура эмес')
        result = await  get_prediction(image_bytes)
        return result

    except Exception as e:
        raise HTTPException(status_code=500 , detail=str(e))