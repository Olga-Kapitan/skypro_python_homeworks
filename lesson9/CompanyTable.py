from sqlalchemy import create_engine
from sqlalchemy.sql import text


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

    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_companies_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id=id).fetchall()

    def get_active_companies(self):
        return self.__db.execute(
            self.__scripts["select only active"]).fetchall()

    def delete_companies(self, id):
        return self.__db.execute(
            self.__scripts["delete by id"], id_to_delete=id)

    def create_company(self, name):
        return self.__db.execute(self.__scripts["insert_new"], new_name=name)

    def get_max_id_company(self):
        return self.__db.execute(self.__scripts["max id company"]).fetchall()[0][0]
