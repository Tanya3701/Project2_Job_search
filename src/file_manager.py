from abc import ABC, abstractmethod
import json
import os
import csv

import pandas as pd


class FileManager(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def write_vacancies(self, *args, **kwargs) -> None:
        """Метод для записи данных в файл"""
        pass

    @abstractmethod
    def load_vacancies(self, *args, **kwargs) -> list[dict]:
        """Метод для получения данных из файла"""
        pass

    @abstractmethod
    def delete_vacancies(self, *args, **kwargs) -> str:
        """Метод удаления данных из файла"""
        pass


class FileManagerJson(FileManager):
    """Класс для работы с файлами json"""

    vacancies = list
    vacancies_path = str
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    data_file = os.path.join(data_dir, "vacancies.json")

    def __init__(self, vacancies_path=data_file) -> None:
        self.__vacancies_path = vacancies_path

    def write_vacancies(self, data_vacancies) -> None:
        """Метод для записи данных в json-файл"""
        full_path = os.path.abspath(self.__vacancies_path)
        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(data_vacancies, f, ensure_ascii=False, indent=4)

    def load_vacancies(self) -> list[dict]:
        """Метод для получения данных из json-файла"""
        full_path = os.path.abspath(self.__vacancies_path)
        with open(
            full_path,
            "r",
            encoding="utf-8",
        ) as f:
            vacancies_list = json.load(f)
            return vacancies_list

    def add_vacancies(self, new_vacancies: list) -> str:
        """добавление вакансии в файл json"""
        with open(self.__vacancies_path, "r", encoding="utf-8") as file:
            old_data = json.load(file)
            add_count = 0
            for item in new_vacancies:
                if item not in old_data:
                    old_data.append(item)
                    add_count += 1
                else:
                    continue
        with open(self.__vacancies_path, "w", encoding="utf-8") as file:
            json.dump(old_data, file, ensure_ascii=False, indent=4)
        if add_count == 0:
            result = "Новых вакансий нет"
        else:
            result = f"Добавлено {add_count} новых вакансий"
        return result

    def delete_vacancies(self, key_words: list) -> str:
        """Метод удаления вакансии из файла по заданному слову"""
        with open(self.__vacancies_path, "r", encoding="utf-8") as file:
            all_data = json.load(file)
            delete_count = 0
            for word in key_words:
                for item in all_data:
                    if (
                        word.lower() in item["Наименование"].lower()
                        or word.lower() in item["Общие требования"].lower()
                    ):
                        all_data.remove(item)
                        delete_count += 1
        with open(self.__vacancies_path, "w", encoding="utf-8") as file:
            json.dump(all_data, file, ensure_ascii=False, indent=4)
        return f"Удалено {delete_count} вакансий"


class FileManagerCsv(FileManager):
    """Класс для работы с файлами csv"""

    vacancies_path = str

    def __init__(self, vacancies_path="../data/vacancies.csv") -> None:
        self.vacancies_path = vacancies_path

    def write_vacancies(self, data_vacancies: list[dict]) -> None:
        """Метод записи данных в файл"""
        with open(self.vacancies_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data_vacancies)

    def load_vacancies(self) -> list[dict]:
        """Метод чтения данных из csv файла"""
        new_list = []
        df = pd.read_csv(self.vacancies_path, dtype={})
        result = df.to_dict()
        for item in result:
            new_list.append(item)
        return new_list

    def delete_vacancies(self, key_words: list) -> str:
        """Метод удаления данных из файла по заданному слову"""
        new_list = []
        df = pd.read_csv(self.vacancies_path, dtype={})
        result = df.to_dict()
        delete_count = 0
        for item in result:
            new_list.append(item)
            for key_word in key_words:
                if key_word.lower() in item.lower():
                    new_list.remove(item)
                    delete_count += 1
        with open(self.vacancies_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(new_list)
        return f"Удалено {delete_count} вакансий"
