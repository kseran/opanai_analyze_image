FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальной код приложения в контейнер
COPY . .

# Укажите команду для запуска вашего приложения
CMD ["python", "main.py"]
