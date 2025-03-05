# variables de entrada
nombre = input('ingrese su nombre: \n')
edad = int(input('edad: \n'))
estrato = int(input('estrato: \n'))
ocupacion = int(input('\n 1: empleado del gobierno \n 2 empleado privado \n 3 desempleado \n'))
diasviviendoenmedellin = int(input('dias viviendo en medellin: \n'))

#variables que voy a utilizar
TOTAL= 0
DESCUENTO=0
FINAL= 0

#condicionales para los estratos
if estrato == 0:
    print('no pagar impuestos')
elif estrato == 1 or 2:
    TOTAL = 500*diasviviendoenmedellin
elif estrato == 3 or 4:
    TOTAL = (50000 * diasviviendoenmedellin) + 1000000
elif estrato == 5 or 6:
    TOTAL = 250000 * diasviviendoenmedellin

#condicionales para descuento
if ocupacion == 1:
    FINAL= TOTAL * 0.50
    DESCUENTO = 50

elif ocupacion == 2:
    FINAL= TOTAL * 0.05
    DESCUENTO = 5

elif ocupacion == 3:
    FINAL =  TOTAL * 0.10
    DESCUENTO = 10

# Resultados finales
print(f'los impuestos totales para {nombre} con {edad} años' )
print(f'Es el valor de ${TOTAL} sin descuento')
print(f'El descuento es del {DESCUENTO}%')
print(f'Con el descuento del estrato el total es de ${FINAL}')