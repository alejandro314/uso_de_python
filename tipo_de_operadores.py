'''

tipo_de_operadores
'''
#operador suma
print(2+6)

#operador resta
print(8-4)

#operador multiplicacion
x=4
y=6
# print(x*y)

#operador division
z=12/4
print(z)
print(type(z)) #el resultado de la division siempre es flotante

#operador division piso(floor)
print (10/3) #division tradicional
print (10/3) #division piso
print (14.5)
print (14.5/3)
'''
la division que siempre devuelve el entero mas proximo abajo
'''

#operacion modulo
print(20/3)
print(20%3)


print (8/-3) #division piso

#operacion potencial
print (x**2)

'''
Operadores de Comparación
Este tipo de operadores los usamos cuando deseamos comparar expresiones o
variables. Python evalúa si se cumple la comparación y nos devuelve (retorna) un
valor True o False
'''

#es igual a
print("enca"=="Enca")

#print(8==8)

print(3==3)

print(3==3.0)

#es diferente de
print("palabra"!="palabra")

'''
operadores de asignacion
'''
#asignacion de igualdad o definicio 
W=5
#incrementeo
saldo_b=200
#saldo= saldo + 1
saldo_b-=8
print(saldo_b)
#decrecimiento
'''
operadores logicos
and:comprueba si todas las condiciones se cumplen, true , false de lo contrario
or:comprueba si alguna de las condiciones se cumplen, true , false de lo contrario
not: negar el estado de una variable
'''
print(x==4 and y==6 )
print(x==5 or y==8)

usuario_logueado=True
click_logout=True
print(not usuario_logueado)