from ConnectionFactory.ConnectionFactory import ConnectionFactory
import pymysql
from Modelo.gato import gato


class gatoDAO:
    def __init__(self, con):
        self.con = con.getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def listar(self):
        query = "SELECT * FROM gatos"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                gato_obj = gato(*row)
                resultados.append(gato_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar gatos: {e}")
            return []
