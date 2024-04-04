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

    def crear(self, gato):
        query = "INSERT INTO gatos(nombre, sexo, disponibilidad, edad, foto) VALUES (%s, %s, %s ,%s, %s)"
        try:
            self.cursor.execute(
                query,
                (
                    gato.getNombre(),
                    gato.getSexo(),
                    gato.getDisponibilidad(),
                    gato.getEdad(),
                    gato.getFoto(),
                ),
            )
            self.con.commit()
            print("Creción de gato con exito")
        except Exception as e:
            print(f"Error al guardar usuario: {e}")
        finally:
            self.close()

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

    def modificar(self, gato):
        query = "UPDATE gatos SET nombre = %s, sexo = %s , disponibilidad = %s, edad = %s , foto = %s WHERE gatoID = %s"
        try:
            self.cursor.execute(
                query,
                (
                    gato.getNombre(),
                    gato.getSexo(),
                    gato.getDisponibilidad(),
                    gato.getEdad(),
                    gato.getFoto(),
                    gato.getId(),
                ),
            )
            self.con.commit()
            self.close()
            print("Michimodificacion correcta")
        except Exception as e:
            print(f"Error al modificar gato: {e}")

    def eliminar(self, gato):
        query = "DELETE FROM gatos WHERE gatoID = %s"
        try:
            self.cursor.execute(
                query, (gato.getId(),)
            )  # Notice the comma after gato.getId()
            self.con.commit()
            self.close()
            print("MichiEliminación exitosa")
        except Exception as e:
            print(f"Error al eliminar gato: {e}")
