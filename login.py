from usuario import Usuario

DOMINIO_EMPRESA = "@buspy.com"

def IniciarSesion(usuarios):
    successful_login = False

    while successful_login == False:
        username = input("Introduce el usuario: ")
        password = input("Introduce la contraseña: ")

        for usuario in usuarios:
            if usuario.getUsername() == username and usuario.getPassword() == password:
                successful_login = True
                
        if successful_login == False:
            print("Usuario o contraseña incorrectos. Intenta de nuevo.")

    return successful_login

def Registro():
    email_correcto = False

    username = input("Introduce el nombre de usuario: ")
    password = input("Introduce la contraseña: ")

    while email_correcto == False:
        email = input("Introduce el correo electrónico: ")
        if email[-10:] == DOMINIO_EMPRESA and email.count("@") == 1 and len(email) > len(DOMINIO_EMPRESA):
            email_correcto = True
        else:
            print("Error. El correo no pertenece al dominio de la empresa")
    

    usuario_nuevo = Usuario(username, password, email)
    return usuario_nuevo