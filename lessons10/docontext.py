import sqlite3 as sql
#from sqlite3 import Connection
class DBContext:
    def __init__(self, database = "", timeout = 5.0):#, conn = Connection
        self.DataBase = database
        self.TimeOut = timeout
        #self.Conn = conn
    def Execute(self, query = ""):
        try:
            connection = sql.connect(self.DataBase, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        except Exception as ex:
            print(ex)
            connection.close()
        finally:
            connection.close()