from ConnectionFactory.ConnectionFactory import ConnectionFactory
import pymysql
from Modelo.platillo import platillo


class platilloDAO:
    def __init__(self, con):
        self.con = con.getConnection()
        self.cursor = self.con.cursor()
    
    def close(self):
        self.cursor.close()
        self.con.close()

    
    def guardar(self, platillo): //para el admin
        var = 1
        query = "INSERT INTO platillos(nombre, descripcion, foto) VALUES (%s, %s,%s)"
        try:
            self.cursor.execute(
                query,
                (
                    platillo.getNombre(),
                    platillo.getDescripcion(),
                    platillo.getFoto(),
                ),
            )
            self.con.commit()
        except mysql.connector.errors.IntegrityError as e:
            var = e.args[0]
        finally:
            self.close()
            return var

    def listar(self): //para desplegarlos en la página
        query = "SELECT * FROM platillos"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                platillo_obj = platillo(*row)
                resultados.append(platillo_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar platillos: {e}")
            return []
    
    def modificar(self, platillo):
        var = 1
        query = "UPDATE platillos SET nombre = %s, descripcion = %s , foto = %s WHERE platilloID = %s"
        try:
            self.cursor.execute(
                query,
                (
                   platillo.getNombre(),
                    platillo.getDescripcion(),
                    platillo.getFoto(),
                    platillo.getId(),
                ),
            )
            self.con.commit()
        except mysql.connector.errors.IntegrityError as e:
            var = e.args[0]
        finally:
            self.close()
            return var
    
     def eliminar(self, platillo):
        var = 1
        query = "DELETE FROM platillos WHERE id = %s"
        try:
            self.cursor.execute(query, (gato.getId(),))
            self.con.commit()
        except mysql.connector.Error as e:
            var = e.args[0]
        finally:
            self.cursor.close()  # Asegúrate de cerrar el cursor si lo has creado aquí
            self.close()
            return var
