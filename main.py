from typing import List
from fastapi import FastAPI, File, UploadFile, Body
from model import ImageResponse, ImageRequest
from analyze_image_openai import analyze_image_openai
from config import Config

app = FastAPI()


@app.post(path="/upload/gpt", response_model=ImageResponse | str)
async def upload_file(image: UploadFile = File(...), list_counters: List[str] = Body(...), key: str = Body(...)):
    """Эндпоинт для загрузки изображения"""
    if key == Config().key:
        response = await analyze_image_openai(ImageRequest(image=image, list_counters=list_counters))
        return ImageResponse(
            img_id=response["id"],
            description=response["data"]
        )
    else:
        return "permission denied"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
