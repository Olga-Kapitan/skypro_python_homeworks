# import requests
import random
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

# создать компанию - получить ее id
# проверка обязательность полей


# получить список сотрудников компании == 0
def test_get_employee_list():
    company = comp_api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]
    list_api = emp_api.get_employee_list(id_company)

    list_db = emp_db.get_list_employee(id_company)

    assert len(list_api) == len(list_db)

    comp_api.delete(id_company)


# добавить нового сотрудника
def test_add_new_employee():
    company = comp_api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]
    print(id_company)

    # my_params = {
    #     "comp_id": str(id_company),
    #     "name": 'Dollie',
    #     "surname": 'Romero',
    #     "my_phone": '778586'
    # }
    # id_company, 'Dollie', 'Romero', '778586'

    emp_db.create_employee(id_company, 'Dollie', 'Romero', '778586')
    id_employee = emp_db.get_list_employee(id_company)[0]["id"]

    list_after = emp_db.get_list_employee(id_company)

    # assert id_employee == list_after[0]['id']
    assert list_after[0]["first_name"] == 'Dollie'
    assert list_after[0]["last_name"] == 'Romero'
    assert list_after[0]["phone"] == '778586'

    emp_db.delete_employee(id_employee)
    comp_api.delete(id_company)


# получить сотрудника по id
def test_get_employee_to_id():
    comp_api.create_company(random.choice(name), random.choice(descr))
    max_id = emp_db.max_id_comp()
    # id_company = company["id"]
    # попробовать по api
    # select max(id) from  company - найти по макс!!
    emp_db.create_employee(max_id, 'Myra', 'Lynch', '556655')
    id_employee = emp_db.get_list_employee(max_id)
    body_db = emp_db.get_employee_by_id(id_employee)

    body_api = emp_api.get_employee_to_id(id_employee)

    assert body_api["id"] == body_db["id"]
    assert body_db["firstName"] == 'Myra'
    assert body_db["lastName"] == 'Lynch'
    assert body_db["phone"] == '556655'

    emp_db.delete_employee(id_employee)
    comp_api.delete(max_id)


# изменить инфо о сотруднике
def test_edit_employee():
    company = comp_api.create_company(random.choice(name), random.choice(descr))
    id_company = company["id"]

    emp_db.create_employee(id_company, 'Myra', 'Lynch', '556655')
    id_employee = emp_db.get_list_employee(id_company)
    body_db = id_employee[0]["id"]
    boby_db_edited = emp_db.edit_employee(id_employee, 'Richards')
    print(body_db)
    print(boby_db_edited)
    # assert id_employee["last_name"] == 'Richards'

    emp_db.delete_employee(id_employee)
    comp_api.delete(id_company)
