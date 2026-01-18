from src.file_manager import FileManagerJson
from src.hh import HH
from src.vacancies import Vacancy


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для исключения вакансий: ").split()

    hh = HH(search_query)
    hh._getting_vacancies()
    vacancy = Vacancy("name", "id_vacancy", 0, 0, "requirement")
    data_v = hh._api_connection("vacancies")
    vacancy.create_vacancy(data_v)
    vacancy.list_dict_vacancies()
    file_manager = FileManagerJson()
    vacancy.list_dict_vacancies()
    vacancies = vacancy.list_dict_vacancies()
    file_manager.write_vacancies(vacancies)
    file_manager.add_vacancies(vacancies)
    file_manager.delete_vacancies(filter_words)
    file_manager.load_vacancies()
    vacancy.get_top_vacancies(top_n)
    top_vacancies = vacancy.get_top_vacancies(top_n)

    for vacancy in top_vacancies:
        print(vacancy)
