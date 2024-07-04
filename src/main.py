from src.api import HHAPI
from src.exceptions import APIException


def main():
    hh = HHAPI()
    hh.text = input("""Введите название вакансии, которую вы ищете
""")
    try:
        data = hh.get_response_data()
    except APIException as e:
        print(f"Ошибка обращения к HHAPI. {e}")


if __name__ == '__main__':
    main()