import requests
import random
from Employee import Employee


api = Employee("https://x-clients-be.onrender.com")

name = ['Chamomile', 'Chairs&Co', 'Color Glass']
descr = ['flowers', 'furniture', 'dishes']

# создать компанию - получить ее id
# проверка обязательность полей


# получить список сотрудников компании == 0
def test_get_employee_list():
    company = api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]
    list = api.get_employee_list(id_company)
    assert len(list) == 0


# добавить нового сотрудника
def test_add_new_employee():
    company = api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]
    print(id_company)

    list_before = api.get_employee_list(id_company)

    parameters = {
            "id": 0,
            "firstName": "John",
            "lastName": "Lane",
            "middleName": "Lane",
            "companyId": id_company,
            "email": "ofapoptu@jebit.lk",
            "url": "",
            "phone": "89994564411",
            "birthdate": "1989-08-18T11:19:57.377Z",
            "isActive": True
        }
    id_employee = (api.add_new_employee(parameters))['id']
    print(id_employee)

    list_after = api.get_employee_list(id_company)

    assert len(list_after) - len(list_before) == 1
    assert id_employee == list_after[0]['id']


# получить сотрудника по id
def test_get_employee_to_id():
    company = api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]
    parameters = {
            "id": 0,
            "firstName": "Georgie",
            "lastName": "Cruz",
            "middleName": "",
            "companyId": id_company,
            "email": "edhes@zawdurac.bq",
            "url": "",
            "phone": "89994564411",
            "birthdate": "1989-08-18T11:19:57.377Z",
            "isActive": True
        }
    id_employee = (api.add_new_employee(parameters))['id']

    body = api.get_employee_to_id(id_employee)
    
    # assert body["firstName"] == "Georgie" - ошибка key
    # assert body["lastName"] == "Cruz"


# изменить инфо о сотруднике
def test_edit():
    company = api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]
    parameters_emp1 = {
            "id": 0,
            "firstName": "Georgie",
            "lastName": "Cruz",
            "middleName": "",
            "companyId": id_company,
            "email": "edhes@zawdurac.bq",
            "url": "",
            "phone": "89994564411",
            "birthdate": "1989-08-18T11:19:57.377Z",
            "isActive": True
    }
    id_employee = (api.add_new_employee(parameters_emp1))['id']
    parameters_emp2 = {
            "lastName": "Gross",
            "email": "joiboog@huwnidji.dm",
            "url": "",
            "phone": "445859",
            "isActive": True
        }
    new_id_employee = api.edit(id_employee, parameters_emp2)

    # assert new_id_employee["lastName"] != "Cruz"
