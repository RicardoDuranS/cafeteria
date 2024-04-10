from Modelo.Solicitud import Solicitud
from Controller.SolicitudController import SolicitudController

sol = Solicitud(
    nombre="Jimenez",
    correo="A017718273@tec",
    telefono="5590990090",
    ciudad="Monterrey",
    gato=27,
)
sol2 = Solicitud(id=3, nombre=None, correo=None, telefono=None, ciudad=None, gato=None)

var = SolicitudController().guardar(sol)
print(var)

var = SolicitudController().eliminar(sol2)
print(var)

for solicitudes in SolicitudController().listar():
    print(solicitudes)
