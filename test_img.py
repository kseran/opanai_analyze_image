import json
import requests


url = "http://127.0.0.1:8000/upload/gpt"
file_path = "false.jpg"
with open(file_path, 'rb') as image:
    files ={'image': (file_path, image.read(), 'image/jpeg')}
list_counters = ['13573191', '15142149', '16132148']
key: str = "629b0f35-acab-4f61-a571-1644b2cdf894"
data = {
        'list_counters': json.dumps(list_counters),
        'key': key
    }
response = requests.post(url, files=files, data=data)
print(response.json())


