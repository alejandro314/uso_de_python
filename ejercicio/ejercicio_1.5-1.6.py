'''
Ejercicio 1.5
Escriba un programa que realice la comprobación
de la división. Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos números, realice la
división entre ellos y entregue al usuario un texto
descriptivo con la comprobación de la división.
'''

#comprobacion de la division

dividendo=float(input("ingrese el dividendo"))
divisor=float(input("ingrese el divisor"))

division=dividendo/divisor

cociente = dividendo / divisor
residuo = dividendo % divisor

print("comprobacion de division")
print(f"{divisor} * {cociente} + {residuo} = {dividendo}")
