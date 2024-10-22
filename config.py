from dotenv import load_dotenv
import os


class Config:
    def __init__(self):
        load_dotenv("./.venv/.env")
        self._prompt: str = "на фото счётчик, ответь мне в формате название и номер вот так: {\"id\":\"Номер счетчика\",\"data\":\"показания счётчика\"}, если значений на фото не найдёшь замени показания и номер счётчика на \"None\" , показания - это либо число на цифровом табло, либо в отедльном окошке где каждая цифра в отдельной рамке, если там есть красные цифры, то их писать не надо, номер счётчика - это один из этих номеров"
        self._model_gpt: str = "gpt-4o-mini"
        self._api_key: str = os.getenv('API_KEY')
        self._key: str = os.getenv('KEY')

    def get_prompt(self, list_counters: list[str]) -> str:
        str_all_counters = ", ".join(list_counters)
        return self._prompt + str_all_counters

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def model_gpt(self):
        return self._model_gpt

    @property
    def key(self):
        return self._key
