import os
from unittest.mock import Mock, patch

from src.file_manager import FileManager, FileManagerJson


def test_init_file_manager_csv(filename_csv):
    assert filename_csv.vacancies_path == "vacancies.csv"


def test_init_file_manager_json(filename_csv):
    assert filename_csv.vacancies_path is not None


@patch("os.path.exists")
def test_write_vacancies(vacancy_list, vacancies):
    vacancies = vacancy_list
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    vacancies_path = os.path.join(data_dir, "vacancies.json")
    mock = Mock(return_value=vacancies_path)
    with patch("builtins.open", mock):
        FileManager.write_vacancies(vacancies)


@patch("os.path.exists")
def test_load_vacancies(vacancy_list, vacancies):
    vacancies = vacancy_list
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    vacancies_path = os.path.join(data_dir, "vacancies.json")
    mock = Mock(return_value=vacancies_path)
    with patch("builtins.open", mock):
        FileManager.load_vacancies(vacancies)


@patch("os.path.exists")
def test_add_vacancies(vacancy_list):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    vacancies_path = os.path.join(data_dir, "vacancies.json")
    mock = Mock(return_value=vacancies_path)
    with patch("builtins.open", mock):
        FileManagerJson.add_vacancies


@patch("os.path.exists")
def test_delete_vacancies(vacancy_list):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    vacancies_path = os.path.join(data_dir, "vacancies.json")
    mock = Mock(return_value=vacancies_path)
    with patch("builtins.open", mock):
        FileManagerJson.delete_vacancies
