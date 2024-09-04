import allure
import random
from faker import Faker
from EmployeeApi import Employee
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable
from EmployeeTable import EmployeeTable

emp_api = Employee("https://x-clients-be.onrender.com")
comp_api = CompanyApi("https://x-clients-be.onrender.com")
comp_db = CompanyTable(
    "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
emp_db = EmployeeTable(
    "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

name = ['Chamomile', 'Chairs&Co', 'Color Glass']
descr = ['flowers', 'furniture', 'dishes']

fake = Faker('ru_RU')
name_e = fake.first_name()
surname_e = fake.last_name()
my_phone_e = fake.postcode()


@allure.id("x-clients - 1")
@allure.story("Работа с карточкой сотрудника")
@allure.feature("READ")
@allure.title("Получение полного списка сотрудников организации")
def test_get_employee_list():
    with allure.step("Создать компанию через Api"):
        company = comp_api.create_company(random.choice(name), random.choice(descr))
    with allure.step("Получить id созданной компании"):
        id_company = company["id"]
    with allure.step("Создать карточку сотрудника"):
        emp_db.create_employee(id_company, name_e, surname_e, my_phone_e)
    with allure.step("Получить список сотрудников из БД"):
        list_emp = emp_db.get_list_employee(id_company)
    with allure.step("Получить список сотрудников из Api"):
        list_db = emp_api.get_employee_list(id_company)
    with allure.step("Получить id сотрудника"):
        id_emp = list_emp[0]["id"]
    with allure.step("Сравнить длину списка сотрудников из БД и Api"):
        assert len(list_emp) == len(list_db)
    with allure.step("Удалить сотрудника из БД"):
        emp_db.delete_employee(id_emp)
    with allure.step("Удалить компанию через Api"):
        comp_api.delete_company(id_company)


@allure.id("x-clients - 2")
@allure.story("Работа с карточкой сотрудника")
@allure.feature("CREATE")
@allure.title("Добавление нового сотрудника")
def test_add_new_employee():
    with allure.step("Создать компанию через Api"):
        company = comp_api.create_company(random.choice(name), random.choice(descr))
    with allure.step("Получить id созданной компании"):
        id_company = company["id"]
    with allure.step("Создать карточку сотрудника"):
        emp_db.create_employee(id_company, name_e, surname_e, my_phone_e)
    with allure.step("Получить список сотрудников из БД"):
        list_emp = emp_db.get_list_employee(id_company)
    with allure.step("Получить id сотрудника"):
        id_employee = list_emp[0]["id"]
    with allure.step("Сравнить корректность заполненных данных"):
        assert id_employee == list_emp[0]['id']
        assert list_emp[0]["first_name"] == name_e
        assert list_emp[0]["last_name"] == surname_e
        assert list_emp[0]["phone"] == my_phone_e
    with allure.step("Удалить сотрудника из БД"):
        emp_db.delete_employee(id_employee)
    with allure.step("Удалить компанию через Api"):
        comp_api.delete_company(id_company)


@allure.id("x-clients - 3")
@allure.story("Работа с карточкой сотрудника")
@allure.feature("READ")
@allure.title("Получение карточки сотрудника по id")
def test_get_employee_to_id():
    with allure.step("Создать компанию через Api"):
        comp_api.create_company(random.choice(name), random.choice(descr))
    with allure.step("Получить максимальный id компании"):
        max_id_company = comp_db.get_max_id_company()
    with allure.step("Создать карточку сотрудника"):
        emp_db.create_employee(max_id_company, name_e, surname_e, my_phone_e)
    with allure.step("Получить максимальный id сотрудника"):
        max_id_employee = emp_db.max_id_emp(max_id_company)
    with allure.step("Получить данные сотрудника по id из БД"):
        body_db = emp_db.get_employee_by_id(max_id_employee)
    with allure.step("Получить данные сотрудника по id из Api"):
        body_api = emp_api.get_employee_to_id(max_id_employee)
    with allure.step("Сравнить корректность заполненных данных"):
        assert body_db[0][0] == body_api["id"]
        # assert body_db[0]["firstName"] == name_e
        # assert body_db[0]["lastName"] == surname_e
        # assert body_db[0]["phone"] == my_phone_e
    with allure.step("Удалить сотрудника из БД"):
        emp_db.delete_employee(max_id_employee)
    with allure.step("Удалить компанию через Api"):
        comp_api.delete_company(max_id_company)


@allure.id("x-clients - 4")
@allure.story("Работа с карточкой сотрудника")
@allure.feature("UPDATE")
@allure.title("Редактирование карточки сотрудника")
def test_edit_employee():
    with allure.step("Создать компанию через Api"):
        company = comp_api.create_company(random.choice(name), random.choice(descr))
    with allure.step("Получить id созданной компании"):
        id_company = company["id"]
    with allure.step("Создать карточку сотрудника"):
        emp_db.create_employee(id_company, name_e, surname_e, my_phone_e)
    with allure.step("Получить id сотрудника"):
        id_employee = emp_db.get_list_employee(id_company)[0]["id"]
    with allure.step("Редактирование карточки сотрудника"):
        emp_db.edit_employee(id_employee, 'Richards')
    with allure.step("Получение списка сотрудников"):
        list_emp = emp_db.get_list_employee(id_company)
    with allure.step("Проверить измененные данные на соответствие"):
        assert list_emp[0]["last_name"] == 'Richards'
    with allure.step("Удалить сотрудника из БД"):
        emp_db.delete_employee(id_employee)
    with allure.step("Удалить компанию через Api"):
        comp_api.delete_company(id_company)
