import re
from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""

    name: str
    id_vacancy: str
    salary_from: int
    salary_to: int
    requirement: str
    vacancies: list[dict]

    __slots__ = [
        "name",
        "id_vacancy",
        "salary_from",
        "salary_to",
        "requirement",
        "vacancies",
        "avg_salary",
    ]

    def __init__(
        self,
        name: str,
        id_vacancy: str,
        salary_from: int,
        salary_to: int,
        requirement: str,
    ):
        self.vacancies = []
        self.name = name
        self.id_vacancy = id_vacancy
        if salary_from is None:
            salary_from = 0
        self.salary_from = salary_from
        if salary_to is None:
            salary_to = 0
        self.salary_to = salary_to
        self.requirement = requirement if requirement else "Без описания"
        self.avg_salary = (
            (salary_to + salary_from) / 2
            if salary_to is not None and salary_from is not None
            else 0
        )
        self.__validate_from()
        self.__validate_to()

    def __validate_from(self):
        if self.salary_from is None:
            self.salary_from = 0

    def __validate_to(self):
        if self.salary_to is None:
            self.salary_to = 0

    def __repr__(self) -> str:
        return (
            f"Наименование: {self.name}\nID: {self.id_vacancy}\nЗаработная плата: "
            f"{(self.salary_from + self.salary_to)/2}\nОбщие требования: {self.requirement}\n\n"
        )

    def create_vacancy(self, data: dict) -> list:
        """Добавляет данные"""
        for item in data:
            if item["snippet"]["requirement"] is not None:
                requirement = re.sub(r"<.*?>", "", item["snippet"]["requirement"])
            else:
                requirement = "Без описания"
            if item["salary"] is not None:
                if item["salary"]["from"] is not None:
                    self.salary_from = item["salary"]["from"]
                else:
                    self.salary_from = 0
                if item["salary"]["to"] is not None:
                    self.salary_to = item["salary"]["to"]
                else:
                    self.salary_to = 0
                obj = Vacancy(
                    item["name"],
                    item["id"],
                    item["salary"]["from"],
                    item["salary"]["to"],
                    requirement,
                )
                self.vacancies.append(obj)
            else:
                obj = Vacancy(item["name"], item["id"], 0, 0, requirement)
                self.vacancies.append(obj)
        return self.vacancies

    def __le__(self, other: Any) -> bool:
        return self.avg_salary <= other.avg_salary

    def __ge__(self, other: Any) -> bool:
        return self.avg_salary >= other.avg_salary

    def list_dict_vacancies(self) -> list[dict]:
        """Добавляет данные в список в виде словарей"""
        list_vacancies = []
        for item in self.vacancies:
            dict_vacancies = {
                "Наименование": item.name,
                "ID": item.id_vacancy,
                "Заработная плата": (item.salary_from + item.salary_to) / 2,
                "Общие требования": item.requirement,
            }
            list_vacancies.append(dict_vacancies)
        return list_vacancies

    def sort_vacancies(self) -> list[dict]:
        """Сортирует по зарплате"""
        self.vacancies.sort(key=lambda obj: obj.avg_salary, reverse=True)
        return self.vacancies

    def get_top_vacancies(self, count: int = 50) -> list[dict]:
        """Формирует список из топ вакансий по зарплате"""
        self.sort_vacancies()
        return self.vacancies[:count]
