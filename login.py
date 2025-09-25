from usuario import Usuario
import re

DOMINIO_EMPRESA = "@buspy.com"

def IniciarSesion(usuarios):
    successful_login = False

    username = input("Introduce el usuario: ")
    password = input("Introduce la contraseña: ")

    for usuario in usuarios:
        if usuario.getUsername() == username and usuario.getPassword() == password:
            successful_login = True
            print("Inicio de sesión correcto\n")
                
    if successful_login == False:
        print("Usuario o contraseña incorrectos. Intenta de nuevo.")

    return successful_login

def Registro():
    email_correcto = False

    username = input("Introduce el nombre de usuario: ")

    requerimientos_password = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"

    correct_password = None
    while correct_password == None:
        password = input("Introduce la contraseña: ")
        correct_password = re.match(requerimientos_password, password)

        if correct_password is None:
            print("Introduce una contraseña segura\n\n1.- Mínimo 8 caracteres\n2.- Una mayúscula\n3.- Una minúscula\n4.- Un dígito\n5.- Un carácter especial")

    while email_correcto == False:
        email = input("Introduce el correo electrónico: ")
        if email[-10:] == DOMINIO_EMPRESA and email.count("@") == 1 and len(email) > len(DOMINIO_EMPRESA):
            email_correcto = True
        else:
            print("Error. El correo no pertenece al dominio de la empresa")
    

    usuario_nuevo = Usuario(username, password, email)
    return usuario_nuevo