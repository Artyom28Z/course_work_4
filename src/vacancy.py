class Vacancy:
    __slots__ = ["__name", "__salary"]

    def __init__(self, name: str, salary: int) -> None:
        self.__name = self.validate_name(name)
        self.__salary = self.__validate_salary(salary)

    def __str__(self) -> str:
        return f"Vacancy: {self.__name}, Salary: {self.__salary}"

    def __repr__(self) -> str:
        return f"Vacancy: {self.__name}, Salary: {self.__salary}"

    @staticmethod
    def __validate_salary(salary: int) -> int:
        return 0 if salary < 0 else salary

    @staticmethod
    def validate_name(name: str) -> str:
        return name if name is not None else "Имя не написано"

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary

    @classmethod
    def create_vacancy(cls, vacancy_data: dict):
        cls(
            name=vacancy_data["name"],
            salary=vacancy_data["salary"],
        )
