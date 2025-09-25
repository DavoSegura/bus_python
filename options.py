from cliente import Cliente
from billete import Billete

def SeleccionarBus(buses):
    print("Selecciona el bus:")
    
    contador_buses = 0
    for bus in buses:
        print(f"{contador_buses}. {bus.getDestino()}")
        contador_buses += 1

    bus_seleccionado = int(input())

    return bus_seleccionado

def ComprarBilletes(buses):
    print("¿Cuál es tu nombre?")
    nombre = input()
    print("¿Cuál es tu apellido?")
    apellido = input()

    cliente = Cliente(nombre, apellido)

    bus_seleccionado = SeleccionarBus(buses)

    status = ''
    tickets_disponibles = buses[bus_seleccionado].getTicketsDisponibles()

    if tickets_disponibles > 0:
        billete = Billete(cliente)
        buses[bus_seleccionado].setTicketsVendidos(True, billete)
        buses[bus_seleccionado].setTicketsDisponibles(True)
        status = f'Se ha vendido su billete'
    else:
        status = f'Error'
    return status

def DevolverBilletes(buses):
    status= ''

    print("¿Cuál es tu nombre?")
    nombre = input()
    print("¿Cuál es tu apellido?")
    apellido = input()


    bus_seleccionado = SeleccionarBus(buses)
    tickets_vendidos = buses[bus_seleccionado].getTicketsVendidos()

    for billete in tickets_vendidos:
        cliente = billete.getCliente()
        if cliente.getNombre() == nombre and cliente.getApellido() == apellido:
            buses[bus_seleccionado].setTicketsVendidos(False, billete)
            buses[bus_seleccionado].setTicketsDisponibles(False)
            status = f'Se devuelto tu billete'
            break
    else:
        status = 'Error'
    return status

def CapacidadesBus(buses):

    bus_seleccionado = SeleccionarBus(buses)

    capacidad = buses[bus_seleccionado].getCapacidad()
    tickets_disponibles = buses[bus_seleccionado].getTicketsDisponibles()
    tickets_vendidos = len(buses[bus_seleccionado].getTicketsVendidos())
    
    status = (f'Total: {capacidad}\nLibre: {tickets_disponibles}\nVendido: {tickets_vendidos}')
    return status
