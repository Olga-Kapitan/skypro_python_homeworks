# import requests
import random
from Employee import Employee
from CompanyApi import CompanyApi

emp_api = Employee("https://x-clients-be.onrender.com")
comp_api = CompanyApi("https://x-clients-be.onrender.com")

name = ['Chamomile', 'Chairs&Co', 'Color Glass']
descr = ['flowers', 'furniture', 'dishes']

# создать компанию - получить ее id
# проверка обязательность полей


# получить список сотрудников компании == 0
def test_get_employee_list():
    company = comp_api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]
    list = emp_api.get_employee_list(id_company)
    assert len(list) == 0

    comp_api.delete(id_company)


# добавить нового сотрудника
def test_add_new_employee():
    company = comp_api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]
    print(id_company)

    list_before = emp_api.get_employee_list(id_company)

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
    id_employee = (emp_api.add_new_employee(parameters))['id']
    print(id_employee)

    list_after = emp_api.get_employee_list(id_company)

    comp_api.delete(id_company)

    assert len(list_after) - len(list_before) == 1
    assert id_employee == list_after[0]['id']


# получить сотрудника по id
def test_get_employee_to_id():
    company = comp_api.create_company(random.choice(name), random.choice(descr))
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
    new_employee = emp_api.add_new_employee(parameters)
    id_employee = new_employee["id"]
    body = emp_api.get_employee_to_id(id_employee)
    print(body)

    comp_api.delete(id_company)

    assert body["firstName"] == "Georgie"
    assert body["lastName"] == "Cruz"
    assert id_employee == body['id']


# изменить инфо о сотруднике
def test_edit_employee():
    company = comp_api.create_company(random.choice(name), random.choice(descr))
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
    employee_emp1 = emp_api.add_new_employee(parameters_emp1)
    id_employee = employee_emp1["id"]
    parameters_emp2 = {
        "lastName": "Gross",
        "email": "joiboog@huwnidji.dm",
        "url": "",
        "phone": "445859",
        "isActive": True
        }
    new_employee = emp_api.edit_employee(id_employee, parameters_emp2)
    print(new_employee)

    comp_api.delete(id_company)

    assert new_employee["email"] == "joiboog@huwnidji.dm"
    assert new_employee["isActive"] == True
