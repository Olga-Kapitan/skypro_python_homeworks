from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


@allure.epic("Сотрудники") 
@allure.severity("blocker")
class EmployeeTable:
    __scripts = {
        "insert_new": text(
            'insert into employee (company_id, first_name, last_name, phone) values (:company_id, :first_name, :last_name, :phone)'),
        "delete by id": text('delete from employee where id =:id_employee'),
        "update": text(
            'update employee set last_name =:last_name where id = :id_employee'),
        "select by id": text('select * from employee where id = :id_employee'),
        "select list": text(
            "select * from employee where company_id = :company_id"),
        "max_id_emp": text(
            "select max(id) from employee where company_id =:company_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("БД. Создание карточки сотрудника {comp_id}. {name} {surname} {my_phone}")
    def create_employee(self, comp_id: int, name: str, surname: str, my_phone: int) -> dict:
        """ Создает карточку сотрудника через БД.
        
            Принимает параметры: id компании, имя сотрудника,
            фамилию и номер телефона.

            Возвращает данные сотрудника в виде словаря
        """
        return self.__db.execute(
            self.__scripts["insert_new"], company_id=comp_id, first_name=name, last_name=surname, phone=my_phone)

    @allure.step("БД. Удаление карточки сотрудника {id_emp}")
    def delete_employee(self, id_emp: int) -> None:
        """ Удаляет карточку сотрудника через БД.

            Принимает параметр: id сотрудника для удаления.
        """
        return self.__db.execute(
            self.__scripts["delete by id"], id_employee=id_emp)

    @allure.step("БД. Редактирование карточки сотрудника {id_emp}. {surname}")
    def edit_employee(self, id_emp: int, surname: str) -> dict:
        """ Редактирует карточку сотрудника через БД.

            Принимает параметры: id сотрудника, новую фамилию сотрудника.

            Возвращает данные сотрудника в виде словаря.
        """
        return self.__db.execute(
            self.__scripts["update"], id_employee=id_emp, last_name=surname)

    @allure.step("БД. Получение карточки сотрудника по {id_emp}")
    def get_employee_by_id(self, id_emp: int) -> dict:
        """ Получает конкретную карточку сотрудника через БД

            Принимает параметры: id сотрудника

            Возвращает данные сотрудника в виде словаря.
        """
        return self.__db.execute(
            self.__scripts["select by id"], id_employee=id_emp).fetchall()

    @allure.step("БД. Получение списка сотрудников в компании {comp_id}")
    def get_list_employee(self, comp_id: int) -> list:
        """ Получает список сотрудников компании через БД.

            Принимает параметры: id компании.

            Возвращает данные сотрудников в виде списка.
        """
        return self.__db.execute(
            self.__scripts["select list"], company_id=comp_id).fetchall()

    @allure.step("БД. Получение максимального {id} сотрудника в компании")
    def max_id_emp(self, id: int) -> dict:
        """ Получает максимальное id сотрудника компании через БД.

            Принимает параметры: id компании.

            Возвращает данные сотрудника в виде словаря.
        """
        return self.__db.execute(
            self.__scripts["max_id_emp"], company_id=id).fetchall()[0][0]
