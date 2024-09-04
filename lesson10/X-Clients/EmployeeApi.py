import requests
import allure


@allure.epic("Сотрудники")
@allure.severity("blocker")
class Employee:

    def __init__(self, url):
        self.url = url

    @allure.step("Api. Получить токен авторизации")
    def get_token(self, user='raphael', password='cool-but-crude') -> str:
        """ Получает токен для авторизации Api"""
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()['userToken']

    @allure.step("Api. Получить список сотрудников в организации c {id}")
    def get_employee_list(self, id: int) -> list:
        """ Получает список сотрудников в конкретной организации через Api.

            Принимает параметр: id компании.

            Возвращает данные сотрудников в виде списка.
        """
        resp = requests.get(self.url + '/employee?company=' + str(id))
        return resp.json()

    @allure.step("Api. Добавить нового сотрудника в организацию")
    def add_new_employee(self, parameters) -> dict:
        """ Добавляет нового сотрудника в организацию через Api/

            Возвращает данные сотрудника в виде словаря.
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/employee', headers=my_headers, json=parameters)
        return resp.json()

    @allure.step("Api. Получить карточку сотрудника по {id}")
    def get_employee_to_id(self, id: int) -> dict:
        """ Получает данные сотрудника через Api.

            Принимает параметр: id компании.

            Возвращает данные сотрудника в виде словаря
        """
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    @allure.step("Api. Редактировать карточку сотрудника {id_employee}")
    def edit_employee(self, id_employee: int, parameters) -> dict:
        """ Редактирует данные сотрудника через Api/

            Принмает параметр: id сотрудника для редактирования.

            Возвращает данные сотрудника в виде словаря
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(
            self.url + '/employee/' + str(
                id_employee), headers=my_headers, json=parameters)
        return resp.json()
