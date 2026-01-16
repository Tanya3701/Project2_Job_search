import pytest

from src.file_manager import FileManagerCsv, FileManagerJson
from src.vacancies import Vacancy


@pytest.fixture()
def first_vacancy():
    return Vacancy(
        "Backend-разработчик",
        "129177346",
        100000,
        150000,
        "Опыт коммерческой разработки на Go",
    )


@pytest.fixture()
def second_vacancy():
    return Vacancy(
        "DevOps Engineer (Intern,Junior)",
        "128000081",
        50000,
        75000,
        "Практический опыт разработки ETL в любом ETL инструменте.",
    )


@pytest.fixture()
def third_vacancy():
    return Vacancy(
        "Инженер базы данных",
        " 128878688",
        150000,
        200000,
        "Умение выстраивать эффективную коммуникацию в команде и объяснять "
        "технические детали не-техническим коллегам.",
    )


@pytest.fixture()
def vacancy_list():
    return [
        {
            "Наименование": "Backend-разработчик",
            "ID": "129177346",
            "Заработная плата": 125000,
            "Общие требования": "Опыт коммерческой разработки на Go",
        },
        {
            "Наименование": "DevOps Engineer (Intern, Junior)",
            "ID": "128000081",
            "Заработная плата": 62500,
            "Общие требования": "Практический опыт разработки ETL в любом ETL инструменте.",
        },
        {
            "Наименование": "Инженер базы данных",
            "ID": "128878688",
            "Заработная плата": 175000,
            "Общие требования": "Умение выстраивать эффективную коммуникацию в команде "
                                "и объяснять технические детали не-техническим коллегам.",
        },
    ]


@pytest.fixture()
def vacancies():
    return [
        {
            "name": "Backend-разработчик",
            "id": "129177346",
            "salary": {"from": 150000, "to": 200000},
            "snippet": {
                "requirement": "Умение выстраивать эффективную коммуникацию в команде"
                               " и объяснять технические детали не-техническим коллегам."
            },
        }
    ]


@pytest.fixture()
def filename_json():
    return FileManagerJson("vacancies.json")


@pytest.fixture()
def filename_csv():
    return FileManagerCsv("vacancies.csv")
