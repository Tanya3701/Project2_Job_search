from abc import ABC, abstractmethod
from typing import Any

import requests


class BaseHH(ABC):
    """Абстрактный класс для получения данных с API"""

    pass

    @abstractmethod
    def __api_connection(self, *args, **kwargs):
        """Метод для соединения с API"""
        pass

    @abstractmethod
    def __getting_vacancies(self, *args, **kwargs):
        """Метод получения списка вакансий"""


class HH(BaseHH, ABC):
    """Класс для работы с платформой hh.ru"""

    base_url: str
    response: requests.Response
    params: dict

    def __init__(self, keyword: str) -> None:
        self.__base_url = "https://api.hh.ru"
        self.__params: dict[str, str | int] = {"text": keyword, "per_page": 100}

    def _BaseHH__api_connection(self, endpoint: str) -> Any | None:
        """Метод для соединения с API и фильтра данных по ключевому слову"""
        try:
            url = f"{self.__base_url}/{endpoint}"
            response = requests.get(url, params=self.__params)
            response.raise_for_status()
            self.__vacancies = response.json()["items"]
            return self.__vacancies
        except requests.exceptions.ConnectionError as e:
            print(e)
            return []

    def _BaseHH__getting_vacancies(self) -> list[dict]:
        """Метод получения списка вакансий"""
        self._BaseHH__api_connection("vacancies")
        return self.__vacancies
