from Controller.UsuarioController import usuarioController
from Modelo.Usuario import usuario as User
from Modelo.Gato import gato
from Controller.GatoController import gatoController

# USER TESTS
# User crear usuario

us = User("Comprador", "L1@kik0p")
controller = usuarioController().crearUsuario(us)
print(controller)

# User validar
us = User("Comprador", "L1@kik0")
resp = usuarioController().validarUser(us)
print(resp)
