from Modelo.usuario import usuario
from ConnectionFactory.ConnectionFactory import ConnectionFactory
import pymysql


class usuarioDAO:
    def __init__(self, con):
        self.con = con.getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def validar(self, usuario):
        query = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
        try:
            self.cursor.execute(query, (usuario.getUsuario(), usuario.getContraseña()))
            resultados = self.cursor.fetchall()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al validar usuario: {e}")
            return []

    def guardar(self, usuario):
        query = "INSERT INTO usuarios(usuario, contraseña) VALUES (%s, %s)"
        try:
            self.cursor.execute(query, (usuario.getUsuario(), usuario.getContraseña()))
            self.con.commit()
            print("Usuario creado con exito")
        except pymysql.IntegrityError as e:
            if e.args[0] == 1062:  # Ensure this is an integer comparison
                print("Usuario existente")
        except Exception as e:
            print(f"Error al guardar usuario: {e}")
        finally:
            self.close()
