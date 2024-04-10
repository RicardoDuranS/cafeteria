from Modelo.Solicitud import Solicitud
from ConnectionFactory.ConnectionFactory import ConnectionFactory
from DAO.SolicitudDAO import SolicitudDAO


class SolicitudController:
    def __init__(self):
        factory = ConnectionFactory()
        self.solicitudDAO = SolicitudDAO(factory)

    def guardar(self, solicitud):
        resp = self.solicitudDAO.guardar(solicitud)
        return resp

    def eliminar(self, solicitud):
        resp = self.solicitudDAO.eliminar(solicitud)
        if resp == 1:
            return "Solicitud eliminada con exito"
        else:
            return resp

    def listar(self):
        return self.solicitudDAO.listar()

    def listar_por_gatos(self):
        return self.solicitudDAO.listar()
