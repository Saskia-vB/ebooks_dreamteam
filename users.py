from e_books_connect import MSDBConnection


class DBClientTable(MSDBConnection):

    def create_client(self, name, email_address, phone):

        return self.sql_query(f"""INSERT INTO Users (Name, email_address, phone_number) 
                              VALUES ('{name}', '{email_address}', '{phone}')""").commit

    def get_by_id(self, val):
        return self.sql_query(str(f"SELECT * FROM Customers WHERE CustomerID = {val}")).fetchall()

    def get_all(self, name=None):
        result_list = []
        if name is None:
            query_result = self.sql_query('SELECT * FROM Users')
        else:
            query_result = self.sql_query(f"SELECT * FROM Users WHERE name LIKE '%{name}%'")
        while True:
            row = query_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

#test
