from src.vacancies import Vacancy

def test_create_vacancy(second_vacancy, vacancies):
   assert str(Vacancy.create_vacancy(second_vacancy, vacancies)) == ('[Наименование: Backend-разработчик\n'
 'ID: 129177346\n'
 'Заработная плата: 175000.0\n'
 'Общие требования: Умение выстраивать эффективную коммуникацию в команде и '
 'объяснять технические детали не-техническим коллегам.\n'
 '\n'
 ']')


def test_init_vacancy(second_vacancy):
    assert second_vacancy.name == 'DevOps Engineer (Intern \ Junior'
    assert second_vacancy.id_vacancy == '128000081'
    assert second_vacancy.salary_to == 75000
    assert second_vacancy.salary_from == 50000
    assert second_vacancy.avg_salary == 62500
    assert second_vacancy.requirement == 'Практический опыт разработки ETL в любом ETL инструменте.'


def test_sort_vacancies(first_vacancy, second_vacancy, third_vacancy):
    vacancies = [first_vacancy, second_vacancy, third_vacancy]
    vacancies[2].sort_vacancies()


def test_get_top_vacancies(first_vacancy, second_vacancy, third_vacancy):
    vacancies = [first_vacancy, second_vacancy, third_vacancy]
    assert vacancies[0].name == 'Backend-разработчик'


def test_list_dict_vacancies(first_vacancy):
    assert Vacancy.list_dict_vacancies(first_vacancy) == []