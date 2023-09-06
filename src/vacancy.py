class Vacancy:
    """ Класс, осуществляющий работу с вакансиями"""
    __slots__ = ("title", "url", "salary", "description")

    def __init__(self, title, url, salary, description):
        self.title: str = title
        self.url: str = url
        self.salary: float = salary['from'] if salary['from'] else salary['to']
        self.description: str = description

    def __str__(self) -> str:
        return f"Название: {self.title}, Ссылка: {self.url}, Зарплата: {self.salary},Описание: {self.description}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__slots__})"

    def __lt__(self, other):
        return int(self.salary) < int(other.salary)

    def __le__(self, other):
        return int(self.salary) <= int(other.salary)

    def __gt__(self, other):
        return int(self.salary) > int(other.salary)

    def __ge__(self, other):
        return int(self.salary) >= int(other.salary)
