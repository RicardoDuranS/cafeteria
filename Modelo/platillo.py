class Platillo:
    def __init__(self, id, nombre, descripcion, foto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.foto = foto

    # Métodos getter para cada atributo

    def getId(self):
        return self.id

    def getNombre(self):
        return self.id

    def getDescripcion(self):
        return self.descripcion

    def getFoto(self):
        return self.foto

    # Setters

    def setId(self, id):
        return self.id

    def setNombre(self, nombre):
        return self.nombre

    def setDescripcion(self, descripcion):
        return self.descripcion

    def setFoto(self, foto):
        return self.foto

    def __str__(self):
        return f"Platillo(id={self.id}, nombre={self.nombre}, descripcion={self.descripcion}, foto={self.foto})"
