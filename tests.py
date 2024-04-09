from Controller.usuarioController import usuarioController
from Modelo.usuario import usuario as User
from Modelo.gato import gato
from Controller.gatoController import gatoController

# USER TESTS
# User crear usuario

us = User("Comprador", "L1@kik0p")
controller = usuarioController().crearUsuario(us)

# User validar
"""
us = User("Comprador", "L1@kik0p")
resp = usuarioController().validarUser(us)
print(resp)
"""
# GATO TESTS
"""
gatoController().modificar(gato)

# gatoController().crear(gato)

gatoController().eliminar(gato)
"""
