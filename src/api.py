from abc import ABC, abstractmethod
from json import JSONDecodeError

import requests
from requests import Response

from src.exceptions import HHAPIException


class API(ABC):
    @property
    @abstractmethod
    def url(self) -> str:
        """

        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_response_data(self) -> list[dict]:
        """

        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def _get_response(self) -> Response:
        """

        :return:
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def _check_status(self) -> bool:
        """

        :return:
        """
        raise NotImplementedError()


class HHAPI(API):
    def __init__(self) -> None:
        self.__text = None
        self.__params = {
            "per_page": 100,
            "search_field": "name",
        }
    @property
    def url(self) -> str:
        """

        :return:
        """
        return "https://api.hh.ru/vacancies"

    @property
    def text(self) -> str:
        """

        :return:
        """
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        """

        :param text:
        :return:
        """
        self.__text = text

    def _get_response(self) -> Response:
        """

        :return:
        """
        if not self.__text:
            raise HHAPIException('Нет поискового запроса')
        self.__params["text"] = self.__text
        return requests.get(self.url, params=self.__params)

    def get_response_data(self) -> list[dict]:
        """

        :return:
        """
        response = self._get_response()
        is_allowed = self._check_status(response)
        if not is_allowed:
            raise HHAPIException(f"Ошибка запроса данных status_code:{response.status_code}, response:{response.text}")
        try:
            return response.json()
        except JSONDecodeError:
            raise HHAPIException(f"Ошибка получения данных, получен не json объект response:{response.text}")


    @staticmethod
    def _check_status(response: Response) -> bool:
        """

        :param response:
        :return:
        """
        return response.status_code == 200