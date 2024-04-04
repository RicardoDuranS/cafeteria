from ConnectionFactory.ConnectionFactory import ConnectionFactory
from DAO.gatoDAO import gatoDAO


class gatoController:
    def __init__(self):
        factory = ConnectionFactory()
        self.gatoDAO = gatoDAO(factory)

    def listar(self):
        return self.gatoDAO.listar()

    def crear(self, gato):
        self.gatoDAO.crear(gato)

    def modificar(self, gato):
        self.gatoDAO.modificar(gato)

    def eliminar(self, gato):
        self.gatoDAO.eliminar(gato)
