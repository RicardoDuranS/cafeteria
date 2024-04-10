class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    # Métodos getter para cada atributo
    def getUsuario(self):
        return self.usuario

    def getContraseña(self):
        return self.contraseña

    # Métodos setter para cada atributo
    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContraseña(self, contraseña):
        self.contraseña = contraseña
