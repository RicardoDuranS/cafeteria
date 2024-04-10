from Modelo.Usuario import Usuario
from ConnectionFactory.ConnectionFactory import ConnectionFactory
import pymysql
import mysql


class UsuarioDAO:
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
        var = 1
        query = "INSERT INTO usuarios(usuario, contraseña) VALUES (%s, %s)"
        try:
            self.cursor.execute(query, (usuario.getUsuario(), usuario.getContraseña()))
            self.con.commit()
        except mysql.connector.errors.IntegrityError as e:
            var = e.args[0]
        finally:
            self.close()
            return var
