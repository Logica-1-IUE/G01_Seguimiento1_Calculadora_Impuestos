## Paso 1° Solicitar datos al usuario
nombre= input ('JERONIMO \n')
edad= int(input('18 '))
estrato = int (input ('4 '))
ocupacion= input ('empleado del gobierno, desempleado o empleado privado')
diasvividosenmedellin= int (input('dias vividos en medellin'))

TOTAL = 0

## Paso 2° Calcular los impuestos conforme el estrato
impuesto_base = 0
if estrato == 0:
    impuesto_base = 0
elif estrato == [1, 2]:
    impuesto_base = 500 * diasvividosenmedellin
elif estrato == [3, 4]:
    impuesto_base = (50000 * diasvividosenmedellin) + 1000000
elif estrato == [5, 6]:
    impuesto_base = 250000 * diasvividosenmedellin

## Paso 3° Condicionales para descuento
if ocupacion == 1:
    FINAL = TOTAL * 50
    DESCUENTO = 50
elif ocupacion == 2:
    FINAL = TOTAL * 5
    DESCUENTO = 5
elif ocupacion == 3:
    FINAL = TOTAL * 10
    DESCUENTO = 10

## Paso 4° Resultados finales 
print(f' Los impuestos totales para {JERONIMO}')
print(f'Valor de $ {TOTAL} sin descuento')
print(f'El descuento es {DESCUENTO}%')
print(f'Valor luego del descuento del estrato el total es de ${FINAL}') 