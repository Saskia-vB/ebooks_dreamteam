from e_books_connect import MSDBConnection


class DbBookTable(MSDBConnection):

    def create_entry(self, title, author, release_date, location):
        return self.sql_query(f"""INSERT INTO Books (title, author, release_date, location)
                               VALUES ('{title}', '{author}', '{release_date}', '{location}')""").commit()

    def get_by_id(self, ids):
        return self.sql_query(f"SELECT * FROM Books WHERE BookID = '{ids}'").fetchone()

    def get_all(self, product_name=None):
        result_list = []
        if product_name is None:
            query_result = self.sql_query('SELECT * FROM Books')
        else:
            query_result = self.sql_query(f"SELECT * FROM Books WHERE Book LIKE '%{product_name}%'")
        while True:
            row = query_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

    def create_book(self, val_1, val_2):
        return self.sql_query(f"""INSERT INTO UserBooks (BookID, Book_text) VALUES ('{val_1}', 
                              '{val_2};""").commit()


# new_book = DbBookTable().create_entry('a', 'b', 'c', 'd')
# print(new_book)
new_search = DbBookTable().get_all()
print(new_search)

#test