#Definir variables
nombre = input('ingrese su nombre completo:\n')
edad = int(input('ingrese su edad actual:\n'))
dias_vividos_en_medellin = int(input('ingrese el # de dias vividos en medellin:\n'))
estrato = int(input('ingrese su estrato (0-6):\n'))
#convertimos a minusculas para evitar errores
ocupacion = input('ingrese su ocupacion:').strip().lower()

A = 0
B = 1
total = 0
#calculo del impuesto segun el estrato
if estrato == 0:
    print('No debe pagar impuestos.')
else:
    if estrato == A or estrato == B:
        total = 500 * dias_vividos_en_medellin
        print(f'Debe pagar $500 por dia vivido en medellin.')
    elif estrato in [3,4]:
        total =(50000* dias_vividos_en_medellin) + 1000000
        print(f'Debe pagar $50.000 por dia vivido en medellin + $1.000.000 de base')
    elif estrato in [5,6]:
        total = 250000 * dias_vividos_en_medellin
        print(f'Debe pagar $250000 por dia vivido en medellin')
    #aplicacion de descuentos segun la ocupacion
    if ocupacion=='empleado del gobierno':
        total*= 0.5 # 50 % de descuento
        print(f'Aplicar un 50% de descuento.')
    elif ocupacion == 'desempleado':
        total*= 0.95 #10% de descuento
        print(f'Aplicar 10% de descuento.')
    elif ocupacion == 'empleado del sector privado':
        total*= 0.95 # 5% de descuento
        print(f'Aplicar 5% de descuento.')
    #mostrar total a pagar 
        print(f'{nombre}, el total a pagar es:${total:,.2f}')
