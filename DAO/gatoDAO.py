from ConnectionFactory.ConnectionFactory import ConnectionFactory
import mysql
from Modelo.gato import gato


class gatoDAO:
    def __init__(self, con):
        self.con = con.getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def registrar(self, gato):
        var = 1
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
        except mysql.connector.errors.IntegrityError as e:
            var = e.args[0]
        finally:
            self.close()
            return var

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
        var = 1
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
        except mysql.connector.errors.IntegrityError as e:
            var = e.args[0]
        finally:
            self.close()
            return var

    def eliminar(self, gato):
        var = 1
        query = "DELETE FROM gatos WHERE gatoID = %s"
        try:
            self.cursor.execute(query, (gato.getId(),))
            self.con.commit()
        except mysql.connector.Error as e:
            var = e.args[0]
        finally:
            self.cursor.close()  # Asegúrate de cerrar el cursor si lo has creado aquí
            self.close()
            return var
