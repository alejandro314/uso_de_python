'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''

#entrada1="8 9" # input("ingrese los numeros del segundo conjunto")
#print(map(int,entrada1)) #  8 9
#print(map(int,entrada1.split())) #8,,9
#print(set(map(int,entrada1.split())))#{8,9}


conjunto1=set(map(int,input("ingrese los numeros del segundo conjunto").split()))
conjunto2=set(map(int,input("ingrese los numeros del segundo conjunto").split()))
union=conjunto1|conjunto2
interseccion=conjunto1 & conjunto2
print(conjunto1, conjunto2, union, interseccion)
