'''
crea una lista de palabras predefinidas y pedir al 
usuario una palabra, indicar si esta en la lista o no.
'''
mi_lista=["enero", "febrero","marzo"]
consulta=input("ingrese el mes a buscar")

if consulta in mi_lista:
    print("la palabra se encuentra en la lista")

if mi_lista.count(consulta)>0:
    print("la palabra se encuentra en la lista")