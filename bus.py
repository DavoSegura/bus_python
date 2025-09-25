class Bus:
    def __init__(self, bCapacidad, destino):
        self.setCapacidad(bCapacidad)
        self.__tickets_vendidos = []
        self.__tickets_disponibles = bCapacidad
        self.__destino = destino

    def getDestino(self):
        return self.__destino

    def setTicketsVendidos(self, isCompra, billete):
        if isCompra == True:
            self.__tickets_vendidos.append(billete)
        else:
            if billete in self.__tickets_vendidos:
                self.__tickets_vendidos.remove(billete)
            else:
                print("Error: Billete no encontrado")

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