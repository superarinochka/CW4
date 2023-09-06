import json


class JSONSaver:
    def __init__(self):
        self.file_path = "vacancy.json"

    def add_vacancy(self, vacancy_data):
        """Дописываем в файл"""
        with open(self.file_path, 'w', encoding="utf-8") as file:
            jsonfile = json.dumps(vacancy_data, indent=4, ensure_ascii=False)
            file.write(jsonfile)

    def get_vacancy(self, criterion):
        """По заданному слову проверяем соответствие и добавляем в словарь"""
        find_vacancies = []
        with open(self.file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        for i in data:
            if criterion in i['title']:
                find_vacancies.append(i)
        return find_vacancies

    def delete_vacancy(self):
        with open(self.file_path, 'w', encoding="utf-8") as file:
            file.write('')
