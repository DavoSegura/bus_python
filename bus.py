class Bus:
    def __init__(self, bCapacidad):
        self.setCapacidad(bCapacidad)
        self.__tickets_vendidos = 0
        self.__tickets_disponibles = bCapacidad

    def setTicketsVendidos(self, isCompra):
        if isCompra:
            self.__tickets_vendidos += 1
        else:
            self.__tickets_vendidos -= 1

    def setTicketsDisponibles(self, isCompra):
        if isCompra:
            self.__tickets_disponibles -= 1
        else:
            self.__tickets_disponibles += 1

    def setCapacidad(self, bCapacidad):
        self.__capacidad = bCapacidad

    def getCapacidad(self):
        return self.__capacidad
    
    def getTicketsVendidos(self):
        return self.__tickets_vendidos
    
    def getTicketsDisponibles(self):
        return self.__tickets_disponibles