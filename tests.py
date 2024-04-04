from Controller.usuarioController import usuarioController
from Modelo.usuario import usuario as User
from Modelo.gato import gato
from Controller.gatoController import gatoController

gato = gato("1", "Efervecente", "mujere", True, 5, "")

gatoController().modificar(gato)
