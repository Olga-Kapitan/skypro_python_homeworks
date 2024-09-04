import requests
import allure


@allure.epic("Компании")
@allure.severity("blocker")
class CompanyApi:

    def __init__(self, url):
        self.url = url

    @allure.step("Api. Получить список компаний")
    def get_company_list(self, params_to_add=None) -> list:
        """Получение полного списка компаний через Api.
        
            Возвращает компании в списке.
        """
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()

    @allure.step("Api. Получить токен авторизации {user}:{password}")
    def get_token(self, user='raphael', password='cool-but-crude') -> str:
        """Получение токена для авторизации через Api"""
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()['userToken']

    @allure.step("Api. Получить компанию по {id}")
    def get_company(self, id: int) -> dict:
        """ Получение конкретной компании через Api.

            Принимает параметр id компании.

            Возвращает данные компании в виде словаря.
        """
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    @allure.step("Api. Создание компании {name}({description})")
    def create_company(self, name: str, description='') -> dict:
        """ Создает компанию через Api.
        
            Принимает парамерты: имя компании и описание.

            Возвращает id новой компании в виде словаря.
        """
        company = {
            'name': name,
            'description': description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/company', json=company, headers=my_headers)
        return resp.json()

    @allure.step("Api. Редактирование компании {new_id} - {new_name}({new_descr})")
    def edit_company(self, new_id, new_name, new_descr) -> dict:
        """ Редактирует созданную компанию через Api.
        
            Принимает парамерты: id компании, новое название и описание.

            Возвращает данные измененной компании в виде словаря.
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(
            self.url + '/company/' + str(new_id), headers=my_headers, json=company)
        return resp.json()

    @allure.step("Api. Удаление компании {id}")
    def delete_company(self, id) -> dict:
        """ Удаляет компанию через Api.
        
            Принимает парамерт id компании для удаления.
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(
            self.url + '/company/delete/' + str(id), headers=my_headers)
        return resp.json()

    @allure.step("Api. (Де)активация компании {id} - {isActive}")
    def set_active_state_company(self, id, isActive) -> dict:
        """ (Де)активирует компанию через Api.
        
            Принимает парамеры: id компании и bool(True/False)
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(
            self.url + '/company/status/' + str(id), headers=my_headers, json={"isActive": isActive})
        return resp.json()
