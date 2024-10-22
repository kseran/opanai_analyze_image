from mimetypes import guess_type
from openai import OpenAI
from typing import Dict
from config import Config
import base64
import os
import json
from model import ImageRequest


async def analyze_image_openai(request: ImageRequest) -> Dict[str, str]:
    """Получает изображение, отправляет его на распознавание в модель chatgpt и возвращает описание изображения"""
    file_content = await request.image.read()
    filepath = os.path.join(request.image.filename)
    with open(filepath, "wb") as f:
        f.write(file_content)
    client = OpenAI(api_key=Config().api_key)
    image_loc_url = local_image_to_data_url(filepath)
    response = client.chat.completions.create(
        model=Config().model_gpt,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": Config().get_prompt(request.list_counters)},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"{image_loc_url}"},
                    },
                ],
            }
        ],
    ).json()
    response = json.loads(response)
    response = json.loads(response['choices'][0]['message']['content'])
    return response


def local_image_to_data_url(image_path):
    """Создаёт локальный url, включающий тип и контент изображения"""
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    return f"data:{mime_type};base64,{base64_encoded_data}"
