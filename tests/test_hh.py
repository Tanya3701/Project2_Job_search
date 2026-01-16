from unittest.mock import patch

from src.hh import HH


@patch("requests.get")
def test__BaseHH__api_connection(mock_get):
    mock_get.return_value.json.return_value = {
        "items": {"work": "работа", "salary": 10000}
    }
    hh = HH("python")
    assert hh._BaseHH__api_connection("vacancies") == {
        "work": "работа",
        "salary": 10000,
    }

    mock_get.assert_called_once_with(
        "https://api.hh.ru/vacancies", params={"text": "python", "per_page": 100}
    )


@patch("requests.get")
def test__BaseHH__getting_vacancies(mock_get):
    mock_get.return_value.json.return_value = {
        "items": {"work": "работа", "salary": 10000}
    }
    hh = HH("python")
    assert hh._BaseHH__getting_vacancies() == {"work": "работа", "salary": 10000}

    mock_get.assert_called_once_with(
        "https://api.hh.ru/vacancies", params={"text": "python", "per_page": 100}
    )
