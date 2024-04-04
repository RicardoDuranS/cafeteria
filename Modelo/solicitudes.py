class Solicitudes:
    def __init__(self, nombre, correo, telefono, ciudad, gato):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.ciudad = ciudad
        self.gato = gato
        self.solicitudID = (
            None  # Este atributo se asignará automáticamente en la base de datos
        )

    # Métodos getter para cada atributo
    def getNombre(self):
        return self.nombre

    def getCorreo(self):
        return self.correo

    def getTelefono(self):
        return self.telefono

    def getCiudad(self):
        return self.ciudad

    def getGato(self):
        return self.gato

    def getSolicitudID(self):
        return self.solicitudID

    # Métodos setter para cada atributo
    def setNombre(self, nombre):
        self.nombre = nombre

    def setCorreo(self, correo):
        self.correo = correo

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    def setGato(self, gato):
        self.gato = gato

    def setSolicitudID(self, solicitudID):
        self.solicitudID = solicitudID
