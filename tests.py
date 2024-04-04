from Controller.usuarioController import usuarioController
from Modelo.usuario import usuario as User
from Modelo.gato import gato
from Controller.gatoController import gatoController

us = User("Jesus", "1234")

##controller = usuarioController().validarUser(us)

x = usuarioController().crearUsuario(us)

print(x)
lista = gatoController().listar()

for i in lista:
    print(i)
