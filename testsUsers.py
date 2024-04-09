from Controller.usuarioController import usuarioController
from Modelo.usuario import usuario as User
from Modelo.gato import gato
from Controller.gatoController import gatoController

# USER TESTS
# User crear usuario

us = User("Comprador", "L1@kik0p")
controller = usuarioController().crearUsuario(us)
print(controller)

# User validar
us = User("Comprador", "L1@kik0")
resp = usuarioController().validarUser(us)
print(resp)
