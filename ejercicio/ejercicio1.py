'''
Ejercicio 1: Operadores Aritméticos

Problema: Escribe un programa que solicite al usuario dos números y 
realice las operaciones de suma, resta, multiplicación, división y módulo.

'''
texto_1 = "calculadora"

num_1 = float(input("ingrese el primer numero"))
num_2 = float(input("ingrese el segundo numero"))     #float ayuda a poder imprimir numeros que no son enteros


suma=num_1+num_2
resta=num_1-num_2
multiplicacion=num_1*num_2
division=num_1/num_2 
modulo=num_1%num_2

print("el resultado es",suma)
print("el resultado es",resta)
print("el resultado es",multiplicacion)
print("el resultado es",division)
print("el resultado es",modulo)