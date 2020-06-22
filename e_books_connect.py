# import pyodbc
# import sqlite3
#
# class MSDBConnection:
#
# # should establish connection with any DB with have in MS_SQL
#     def __init__(self, database='EBooks'):
#         self.server = 'localhost'
#         self.database = database
#         self.username = 'root'
#         self.password = 'Figgis03!'
#         self.con = self._establish_connection()
#         self.cursor = self.con.cursor()
#
#     def _establish_connection(self):
#         connection = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=' + self.server + ';''DATABASE='
#                                     + self.database + ';''UID='+self.username+';''PWD='+self.password)
#         return connection
#
#     def sql_query(self, sql_string):
#
#         return self.cursor.execute(sql_string)

#test