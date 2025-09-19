class Cliente:
    def __init__(self, nombre, apellido):
        self.setNombre(nombre)
        self.setApellido(apellido)

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido