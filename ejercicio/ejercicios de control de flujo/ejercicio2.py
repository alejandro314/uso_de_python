'''
solicitar una edad y clasificarla en menores de edad(0-17),
adultos(18-64),adultos mayores(65+)
para este ejercicio usar if elif else y tambien match/case
'''

menor_de_edad=range(0,17)
adultos=range(18,64)
adultos_mayores=range(65,100)
edad=int(input("ingrese su edad"))
if edad in menor_de_edad:
    print("eres menor de edad")
elif edad in adultos:
    print("eres adulto")
else:
    print("eres anciano")