from src.vacancy import Vacancy


def get_vacancies_instances(vacancies: list[dict]) -> list[Vacancy]:
    """

    :param vacancies:
    :return:
    """
    return [Vacancy.create_vacancy(vacancy) for vacancy in vacancies]


def sort_vacancies(vacancies: list[dict]) -> list[Vacancy]:
    return sorted(vacancies, reverse=True)

def convert_salary(vacancies_data: list[Vacancy], response_salary_currency: dict) -> list[Vacancy]:
    for vacancy in vacancies_data:
        currency_coef = response_salary_currency.get(vacancy.currency)
        vacancy.salary = vacancy.salary * currency_coef
    return vacancies_data
