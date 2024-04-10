from ConnectionFactory.ConnectionFactory import ConnectionFactory
from DAO.PlatilloDAO import PlatilloDAO


class PlatilloController:
    def __init__(self):
        factory = ConnectionFactory()
        self.platilloDAO = PlatilloDAO(factory)

    def listar(self):
        return self.platilloDAO.listar()

    def guardar(self, platillo):
        resp = self.platilloDAO.guardar(platillo)
        if resp == 1:
            return "Registro exitoso"
        elif resp == 1062:
            return "Registro duplicado"
        else:
            return resp

    def modificar(self, platillo):
        resp = self.platilloDAO.modificar(platillo)
        if resp == 1:
            return "Modificación exitoso"
        else:
            return resp

    def eliminar(self, platillo):
        resp = self.platilloDAO.eliminar(platillo)
        if resp == 1:
            return "Eliminación exitosa"
        else:
            return resp
