import getpass

#Base de datos
usuario_Correcto = "usuariobonito77"
clave_correcta = "fresasBonitas"

#intentos permitidos
intentos_usuario = 3
usuario_valido = False 

# este while valida el usuario 
while intentos_usuario > 0:
    usuario_ingresado = input("Introduce tu usuario: ")
    if usuario_ingresado == usuario_Correcto:
        print("usuario correcto.")
        usuario_valido = True
        break
    else:
        intentos_usuario -= 1

        print(f"ID incorrecto. Te quedan {intentos_usuario} intento(s).")
# este while valida la clave
if usuario_valido:
    intentos_clave = 3  
    while intentos_clave > 0:
        clave_ingresada = getpass.getpass("Introduce tu clave de acceso: ") 
        if clave_ingresada == clave_correcta:
            print("¡Bienvenido, Acceso permitido!")
            break
        else:
            intentos_clave -= 1
            print(f"clave incorrecta. Te quedan {intentos_clave} intento(s).")
# Aca se terminan los intentos permitidos en caso de fallar
    if intentos_clave == 0:
        print("Has fallado 3 veces la clave. Acceso denegado.")
else:
    print("Has fallado 3 veces la clave. Acceso denegado.")
