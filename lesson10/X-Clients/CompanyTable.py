from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


@allure.epic("Компании") 
@allure.severity("blocker")
class CompanyTable:
    __scripts = {
        "select": "select * from company",
        "select by id": text("select * from company where id =:select_id"),
        "select only active": "select * from company where \"is_active\" = true and deleted_at is null",
        "delete by id": text("delete from company where id =:id_to_delete"),
        "insert_new": text("insert into company (\"name\") values (:new_name)"),
        "insert_new_descr": text("insert into company (\"name\") values (:new_name)"),
        "max id company": "select max(id) from company"
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("БД. Получить список компаний")
    def get_companies(self) -> list:
        """ Получить список компаний через БД
        
            Возвращает данные в виде списка
        """
        return self.__db.execute(self.__scripts["select"]).fetchall()

    @allure.step("БД. Получить компанию по {id}")
    def get_companies_by_id(self, id: int) -> list:
        """ Получить данные конкретной компании через БД.
        
            Принимает параметр id компании.

            Возвращает данные компании в виде списка.
        """
        return self.__db.execute(self.__scripts["select by id"], select_id=id).fetchall()

    @allure.step("БД. Получить список активных компаний")
    def get_active_companies(self) -> list:
        """ Получить список активных компаний через БД.
        
            Возвращает компании в виде списка
        """
        return self.__db.execute(
            self.__scripts["select only active"]).fetchall()

    @allure.step("БД. Удаление компании {id}")
    def delete_companies(self, id: int) -> None:
        """ Удаляет компанию через БД.
        
            Принимает параметр id компании для удаления.
        """
        return self.__db.execute(
            self.__scripts["delete by id"], id_to_delete=id)

    @allure.step("БД. Создание компании {name}")
    def create_company(self, name: str) -> dict:
        """ Создает компанию через БД.
        
            Принимает парамерт: имя(название) компании.

            Возвращает данные и id новой компании.
        """
        return self.__db.execute(self.__scripts["insert_new"], new_name=name)

    @allure.step("БД. Получить максимальный id компании")
    def get_max_id_company(self) -> int:
        """ Получить максимальный id из созданных компаний через БД.
        
            Возвращает max id компании.
        """
        return self.__db.execute(self.__scripts["max id company"]).fetchall()[0][0]
