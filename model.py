from typing import List
from fastapi import UploadFile, File, Body
from pydantic import BaseModel


class ImageResponse(BaseModel):
    """Модель ответа апи"""
    img_id: str
    description: str


class ImageRequest(BaseModel):
    """Модель запроса к апи"""
    image: UploadFile = File(...)
    list_counters: List[str] = Body(...)
