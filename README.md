# Приложение для работы с данными 


## Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Содержание:
### Главная страница
#### Функционал:
* class BaseHH(ABC):

 """Абстрактный класс для получения данных с API"""
* __api_connection(self, *args, **kwargs):

"""Метод для соединения с API"""
* __getting_vacancies(self, *args, **kwargs):

"""Метод получения списка вакансий"""

class HH(BaseHH, ABC):

"""Класс для работы с платформой hh.ru"""
* _BaseHH__api_connection(self, endpoint: str)

"""Метод для соединения с API и фильтра данных по ключевому слову"""
* _BaseHH__getting_vacancies(self)

"""Метод получения списка вакансий"""
* class Vacancy:

"""Класс для работы с вакансиями"""
* create_vacancy(self,data):

"""Добавляет данные"""
* list_dict_vacancies(self):

"""Добавляет данные в список в виде словарей"""
*  sort_vacancies(self):

"""Сортирует по зарплате"""
* get_top_vacancies(self, count=50):

"""Формирует список из топ вакансий по зарплате"""
* class FileManager(ABC):

"""Абстрактный класс для работы с файлами"""
*  write_vacancies(self, *args, **kwargs):

"""Метод для записи данных в файл"""
*  load_vacancies(self, *args, **kwargs):

"""Метод для получения данных из файла"""
* delete_vacancies(self, *args, **kwargs):

"""Метод удаления данных из файла"""
* FileManagerJson(FileManager):

"""Класс для работы с файлами json"""
*  write_vacancies(self, data_vacancies):

"""Метод для записи данных в json-файл"""
* load_vacancies(self):

"""Метод для получения данных из json-файла"""
*  add_vacancies(self, new_vacancies):

"""добавление вакансии в файл json"""
*  delete_vacancies(self, key_words):

"""Метод удаления вакансии из файла по заданному слову"""
* class FileManagerCsv(FileManager):

"""Класс для работы с файлами csv"""
* write_vacancies(self, data_vacancies):

"""Метод записи данных в файл"""
*  load_vacancies(self):

"""Метод чтения данных из csv файла"""
* class FileManagerCsv(FileManager):

"""Класс для работы с файлами csv"""
* delete_vacancies(self, key_words: list)

"""Метод удаления данных из файла по заданному слову"""
*  user_interaction():

"""Функция для взаимодействия с пользователем"""
*  main():

"""Запускает все функциональности"""

 coverage: platform win32, python 3.13.7-final-0 _________________________________________________________________

Name_____________________Cover

src\__init__.py_________________100%

src\file_manager.py____________36%

src\hh.py____________________87%

src\vacancies.py______________79%

tests\__init__.py_________________100%

tests\conftest.py________________92%

tests\test_file_manager.py________100%

tests\test_hh.py________________100%

tests\test_vacancies.py__________100%

------------------------------------------------
TOTAL   _____________________ 72%

