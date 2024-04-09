from Modelo.solicitud import solicitud
from ConnectionFactory.ConnectionFactory import ConnectionFactory
from DAO.solicitudDAO import solicitudDAO


class solicitudController:
    def __init__(self):
        factory = ConnectionFactory()
        self.solicitudDAO = solicitudDAO(factory)

    def guardar(self, solicitud):
        resp = self.solicitudDAO.guardar(solicitud)
        if resp == 1:
            return "Guardado de solicitud exitoso"
        else:
            return resp

    def eliminar(self, solicitud):
        self.solicitudDAO.eliminar(solicitud)

    def listar(self):
        self.solicitudDAO.listar(solicitud)

    def listar_por_gatos(self):
        self.solicitudDAO.listar(solicitud)
