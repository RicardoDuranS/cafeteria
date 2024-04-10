from Modelo.Gato import Gato
from Controller.GatoController import GatoController
import json


# GATO TESTS
mi_gato = Gato(
    id=1, nombre="OptimusSSS", sexo=True, disponibilidad=True, edad=7, foto=""
)
gato2 = Gato(nombre="OptimusModMMMM", sexo=True, disponibilidad=True, edad=7, foto="")

gato3 = Gato(nombre="Megatron", sexo=True, disponibilidad=True, edad=0, foto="")

# print(GatoController().registrar(gato2))
print(GatoController().registrar(gato3))

# GatoController().modificar(mi_gato)

# print(GatoController().eliminar(mi_gato))

gatos = GatoController().listar()

# for gato in gatos:
#   print(gato)

lista_gatos_dict = [gato.to_dict() for gato in gatos]

json_gatos = json.dumps(lista_gatos_dict)
print(json_gatos)
