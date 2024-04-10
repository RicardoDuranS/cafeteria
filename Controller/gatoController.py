from ConnectionFactory.ConnectionFactory import ConnectionFactory
from DAO.GatoDAO import GatoDAO


class GatoController:
    def __init__(self):
        factory = ConnectionFactory()
        self.gatoDAO = GatoDAO(factory)

    def listar(self):
        return self.gatoDAO.listar()

    def registrar(self, gato):
        resp = self.gatoDAO.registrar(gato)
        if resp == 1:
            return "Registro exitoso"
        elif resp == 1062:
            return "Registro duplicado"
        else:
            return resp

    def modificar(self, gato):
        resp = self.gatoDAO.modificar(gato)
        if resp == 1:
            return "Modificación exitoso"
        else:
            return resp

    def eliminar(self, gato):
        resp = self.gatoDAO.eliminar(gato)
        if resp == 1:
            return "Eliminación exitosa"
        else:
            return resp
