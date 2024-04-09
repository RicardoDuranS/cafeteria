from ..Controller import usuarioController
from ..Modelo.usuario import usuario as User
from ..Modelo.gato import gato
from ..Controller.gatoController import gatoController

user = User("rafaes", "kasjdfhk")

resp = usuarioController.validarUser(user)
print(resp)
