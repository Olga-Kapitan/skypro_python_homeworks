import requests


class ToDoList:

    def __init__(self, url='https://todo-app-sky.herokuapp.com/'):
        self.url = url

# Создание.
    def create_task(self, title, completed='null'):
        parameters = {
            'title': title,
            'completed': completed
        }
        result = requests.post(self.url, json=parameters)
        return result.json()

# Переименование.
    def edit_task(self, id_task, title, completed='null'):
        parameters = {
            'title': title,
            'completed': completed
        }
        result = requests.patch(self.url + str(id_task), json=parameters)
        return result.json()

# Удаление.
    def delete_task(self, id_task):
        result = requests.delete(self.url + str(id_task))
        return result.json()

# Получение списка.
    def get_list_task(self):
        result = requests.get(self.url)
        return result.json()

# Получение конкретной задачи из списка.
    def get_info_task(self, id_task):
        result = requests.get(self.url + str(id_task))
        return result.json()

# Отметка задачи «Выполнена».
    def task_done(self, completed='true'):
        result = requests.patch(self.url, json=completed)
        return result.json()

# Снятие отметки «Выполнена».
    def task_unchecking(self, completed='false'):
        result = requests.patch(self.url, json=completed)
        return result.json()
