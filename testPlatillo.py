from Modelo.Platillo import Platillo
from Controller.PlatilloController import PlatilloController

plati = Platillo(
    nombre="Pasta",
    id="1",
    descripcion="Pasta hervida a su punto, con albóndigas",
    foto="",
)

plati2 = Platillo(id=4, nombre="Platillo deli", descripcion="x", foto="")

# controller = PlatilloController().guardar(plati2)
# print(controller)

print(PlatilloController().eliminar(plati2))

controller = PlatilloController().listar()

for sol in controller:
    print(sol)
