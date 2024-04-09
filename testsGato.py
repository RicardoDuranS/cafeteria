from Modelo.gato import gato
from Controller.gatoController import gatoController

# GATO TESTS
mi_gato = gato(
    id=1, nombre="OptimusSSS", sexo=True, disponibilidad=True, edad=7, foto=""
)
gato2 = gato(nombre="OptimusModMMMM", sexo=True, disponibilidad=True, edad=7, foto="")

print(gatoController().registrar(gato2))

gatoController().modificar(mi_gato)

print(gatoController().eliminar(mi_gato))

for gato in gatoController().listar():
    print(gato)
