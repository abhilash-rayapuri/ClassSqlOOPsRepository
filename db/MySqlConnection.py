import mysql.connector as mysqlConn

class MySqlConnection:
    def __init__(self):
        self.connection = mysqlConn.connect(
            host='localhost',
            user='root',
            password='12345678',
            database='company'
        )

    def get_connection(self):
        return self.connection