import requests
import io
from fastapi import HTTPException
from config import config


async  def get_prediction(images_bytes: bytes):
    try:
        print('сурот кетти')
        url = config.ROBOFLOW_URL
        files = {
            'file':('image.jpg,',io.BytesIO(images_bytes),'image/jpg')
        }
        response = requests.post(url,files=files)
        print(response.text)

        if response.status_code != 200:
            raise  HTTPException(status_code=500 , detail="ошибка в сервере")

        return {'confidence':response.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

