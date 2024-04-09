from ConnectionFactory.ConnectionFactory import ConnectionFactory
import mysql
from Modelo.solicitud import Solicitud


class solicitudDAO:
    def __init__(self, con):
        self.con = con.getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def guardar(self, solictud):
        val = 1
        query = "INSERT INTO solicitudes(nombre, correo, telefono, ciudad, gato) VALUES (%s, %s, %s ,%s, %s)"
        try:
            self.cursor.execute(
                query,
                (
                    solictud.getNombre(),
                    solictud.getCorreo(),
                    solictud.getTelefono(),
                    solictud.getCiudad(),
                    Solicitud.getGato(),
                ),
            )
            self.con.commit()
        except mysql.connector.errors.IntegrityError as e:
            var = e.args[0]
        finally:
            self.close()
            return val

    def listar(self):
        query = "SELECT * FROM solicitudes"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                solicitud_obj = Solicitud(*row)
                resultados.append(solicitud_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar las solicitudes: {e}")
            return []

    def listar_por_gatos(self, gato):
        query = "SELECT * FROM solicitudes WHERE gato == %s"
        try:
            self.cursor.execute(query, (gato.getId()))
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                solicitud_obj = Solicitud(*row)
                resultados.append(solicitud_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar las solicitudes: {e}")
            return []
