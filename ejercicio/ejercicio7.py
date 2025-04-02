'''
Problema: Almacenar los nombres de 3 ciudades en una tupla y luego mostrar:

    La primera y la última ciudad.

    La cantidad de caracteres de cada ciudad.
'''

ciudades=("palmira","cali","pradera")
print(ciudades[0],ciudades[-1])
print(f"{ciudades} tiene{len(ciudades)}elementos")
print(len(ciudades[0]),len(ciudades[1]),len(ciudades[2]))