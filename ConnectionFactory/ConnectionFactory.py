import mysql.connector
from mysql.connector import Error


class ConnectionFactory:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "12345678"
        self.database = "michicaf"
        self.connection = None

    def getConnection(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
                if self.connection.is_connected():
                    print("Conexión exitosa a la base de datos")
            except Error as e:
                print(f"Error al conectar a la base de datos: {e}")
        return self.connection
