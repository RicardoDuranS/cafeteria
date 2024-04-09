class gato:
    def __init__(
        self, id=None, nombre=None, sexo=None, disponibilidad=None, edad=None, foto=None
    ):
        self.id = id
        self.nombre = nombre
        self.sexo = sexo
        self.disponibilidad = disponibilidad
        self.edad = edad
        self.foto = foto

    # Getters
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getSexo(self):
        return self.sexo

    def getDisponibilidad(self):
        return self.disponibilidad

    def getEdad(self):
        return self.edad

    def getFoto(self):
        return self.foto

    # Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setSexo(self, sexo):
        self.sexo = sexo

    def setDisponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

    def setEdad(self, edad):
        self.edad = edad

    def setFoto(self, foto):
        self.foto = foto

    def __str__(self):
        return f"Gato(id={self.id}, nombre={self.nombre}, edad={self.edad})"

    # Getters
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getSexo(self):
        return self.sexo

    def getDisponibilidad(self):
        return self.disponibilidad

    def getEdad(self):
        return self.edad

    def getFoto(self):
        return self.foto

    # Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setSexo(self, sexo):
        self.sexo = sexo

    def setDisponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

    def setEdad(self, edad):
        self.edad = edad

    def setFoto(self, foto):
        self.foto = foto

    def __str__(self):
        return f"Gato(id={self.id}, nombre={self.nombre}, edad={self.edad})"
