'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''

productos={
    "pera": 50,
    "manzana": 200,
    "guayaba": 80
}
producto=input("por favor ingrese el nombre")
precio=float(input("por favor ingrese el precio"))

#productos[producto]=precio   #forma 1
#productos.update()
#print(productos)
productos.update({producto:precio, "limon":80})   #forma 2
print(productos)