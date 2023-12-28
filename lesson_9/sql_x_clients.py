from sqlalchemy import create_engine, inspect, text


class TableEmployee:

    def __init__(self, db_con_str):
        self.db_con_str = db_con_str
        self.connect = create_engine(self.db_con_str).connect()

    def get_employees_info_with_phone(self, phone):
        # SQL-запрос SELECT
        sql_query = text(f"SELECT * FROM employee WHERE phone = '{phone}'")

        # Выполнение запроса и получение результатов
        result = self.connect.execute(sql_query)

        # Получение всех строк результатов
        row = result.fetchall()
        return row

    def get_employees_info_with_company_id(self, com_id):
        # SQL-запрос SELECT
        sql_query = text(f"SELECT * FROM employee WHERE company_id = {com_id}")

        # Выполнение запроса и получение результатов
        result = self.connect.execute(sql_query)

        # Получение всех строк результатов
        row = result.fetchall()
        return row

    def get_employee_by_id(self, emp_id):
        # SQL-запрос SELECT
        sql_query = text(f"SELECT * FROM employee WHERE id = {emp_id}")

        # Выполнение запроса и получение результатов
        result = self.connect.execute(sql_query)

        # Получение всех строк результатов
        row = result.fetchall()
        return row

    def delete_employee(self, emp_id):
        # SQL-запрос SELECT
        sql_query = text(f"DELETE FROM employee WHERE id = {emp_id}")

        # Выполнение запроса и получение результатов
        result = self.connect.execute(sql_query)
