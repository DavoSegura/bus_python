from cliente import Cliente
from billete import Billete

def SeleccionarBus(buses):
    print("Selecciona el bus:")
    
    contador_buses = 0
    for bus in buses:
        print(f"{contador_buses}. {bus.getDestino()}")
        contador_buses += 1

    isInputcorrecto = False
    while isInputcorrecto == False:
        bus_seleccionado = input()

        if bus_seleccionado.isnumeric():
            bus_seleccionado = int(bus_seleccionado)
            if 0 <= bus_seleccionado <   len(buses):
                isInputcorrecto = True
            else:
                print("Introduce un número correcto")
        else:
            print("Introduce un número")
        
    return bus_seleccionado

def ComprarBilletes(buses):
    print("¿Cuál es tu nombre?")
    nombre = input()
    print("¿Cuál es tu apellido?")
    apellido = input()

    cliente = Cliente(nombre, apellido)

    bus_seleccionado = SeleccionarBus(buses)

    status = ''
    billetes_disponibles = buses[bus_seleccionado].getBilletesDisponibles()

    if billetes_disponibles > 0:
        billete = Billete(cliente)
        buses[bus_seleccionado].setBilletesVendidos(True, billete)
        buses[bus_seleccionado].setBilletesDisponibles(True)
        status = f'Se ha vendido su billete'
    else:
        status = f'Error: La compra no ha sido realizada'
    return status

def DevolverBilletes(buses):
    status= ''

    print("¿Cuál es tu nombre?")
    nombre = input()
    print("¿Cuál es tu apellido?")
    apellido = input()


    bus_seleccionado = SeleccionarBus(buses)
    billetes_vendidos = buses[bus_seleccionado].getBilletesVendidos()

    for billete in billetes_vendidos:
        cliente = billete.getCliente()
        if cliente.getNombre() == nombre and cliente.getApellido() == apellido:
            buses[bus_seleccionado].setBilletesVendidos(False, billete)
            buses[bus_seleccionado].setBilletesDisponibles(False)
            status = f'Se devuelto tu billete'
            break
    else:
        status = 'Error: No se ha podio devolver su billete'
    return status

def CapacidadesBus(buses):

    bus_seleccionado = SeleccionarBus(buses)

    capacidad = buses[bus_seleccionado].getCapacidad()
    billetes_disponibles = buses[bus_seleccionado].getBilletesDisponibles()
    billetes_vendidos = len(buses[bus_seleccionado].getBilletesVendidos())
    
    status = (f'Total: {capacidad}\nLibre: {billetes_disponibles}\nVendido: {billetes_vendidos}')
    return status
