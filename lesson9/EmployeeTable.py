from sqlalchemy import create_engine
from sqlalchemy.sql import text


class EmployeeTable:
    __scripts = {
        "insert_new": text('insert into employee (company_id, first_name, last_name, phone) values (:company_id, :first_name, :last_name, :phone)'),
        "delete by id": text('delete from employee where id =:id_employee'),
        "update": text('update employee set last_name =:last_name where id = :id_employee'),
        "select by id": text('select * from employee where id = :id_employee'),
        "select list": text("select * from employee where company_id = :company_id"),
        "max_id_emp": text("select max(id) from employee where company_id =:company_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

# создание
    def create_employee(self, comp_id, name, surname, my_phone):
        return self.__db.execute(self.__scripts["insert_new"], company_id=comp_id, first_name=name, last_name=surname, phone=my_phone)

# удаление
    def delete_employee(self, id_emp):
        return self.__db.execute(
            self.__scripts["delete by id"], id_employee=id_emp)

# редактирование
    def edit_employee(self, id_emp, surname):
        return self.__db.execute(
            self.__scripts["update"], id_employee=id_emp, last_name=surname)

# получение записи по id
    def get_employee_by_id(self, id_emp):
        return self.__db.execute(
            self.__scripts["select by id"], id_employee=id_emp).fetchall()

# получение списка
    def get_list_employee(self, comp_id):
        return self.__db.execute(
            self.__scripts["select list"], company_id=comp_id).fetchall()

    def max_id_emp(self, id):
        return self.__db.execute(
            self.__scripts["max_id_emp"], company_id=id).fetchall()[0][0]
