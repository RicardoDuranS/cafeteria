from ConnectionFactory.ConnectionFactory import ConnectionFactory
from DAO.usuarioDAO import usuarioDAO


class usuarioController:
    def __init__(self):
        factory = ConnectionFactory()
        self.usuarioDAO = usuarioDAO(factory)

    def validarUser(self, usuario):
        if self.usuarioDAO.validar(usuario):
            return True
        else:
            return False

    def crearUsuario(self, usuario):
        val = self.usuarioDAO.guardar(usuario)
        if val == 1:
            return "Usuario creado con exito"
        elif val == 1062:
            return "Usuario ya existente favor de ingresar otro"
        else:
            return val
