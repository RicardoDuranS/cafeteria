from Controller.usuarioController import usuarioController
from Modelo.usuario import usuario as User
from Modelo.gato import gato
from Controller.gatoController import gatoController

gato = gato("6", "Efervecente", "mujere", True, 5, "")

user = ("rafaes", "kasjdfhk")

usuarioController().validarUser(user)

gatoController().modificar(gato)

# gatoController().crear(gato)

gatoController().eliminar(gato)
