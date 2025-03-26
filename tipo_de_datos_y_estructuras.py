
'''
tipo de datos strings:cadena de texto <class 'str'>
'''
#dato="enca24"
#dato_2='enca24'

#print(type(dato))
#print(type(dato_2))
#concatenacion de strings
texto_1="programa"

texto_2="desarrollador junior"

enunciado=texto_1 + texto_2
print(enunciado)

#indexacion de strings
#la indexacion se refiere a acceder a un elemento de una cadena en una posicion

nombre="alejandro"
#print(nombre[:])
'''
python es un lenguaje indexado en cero
'''
#print(nombre[5])
#print(nombre[-3])
#slicing de cadenas (porcion de la cadena)
#print(nombre[0:3]) # esta forma de porcionar no incluye el extremo derecho
#print(nombre[2:4])
#print(nombre[0:-5])
'''
tipos de datos numericos
<class 'int'> : se refiere a numeros enteros
<class 'float'> : se refiere a numeros flotantes que contienen decimales
'''
x=5
print(type(x))
y=5.0
#print(type(y))

'''
1.0 False/True
datos boolean
True
False
'''
asistencia=True
#print(type(asistencia))
#print(not asistencia)
'''
tipos de estructuras y metodos
sets:se definen en python con {}
tuplas:se definen en python con()
listas:se definen en python con[]
diccionarios:se definen en python con{'clave':'valor','clave_2':'valor_2´,,}
'''
#sets o conjuntos
'''
se utilizan para almacenar informacion cuando no interesa la posicion 
no permite valores duplicados
'''
conjunto_1={"a","b","c"}
conjunto_2={"d","e","f"}
#print(type(conjunto_1))
#print(conjunto_1)
'''
los metodos indican las cosas que podemos hacer con los objetos
'''

#metodos de los conjuntos
conjunto_1.add("h")
#print(conjunto_1)


#conjunto_2.remove("h")
#print(conjunto_2)

conjunto_3=conjunto_1.union(conjunto_2)
#print(conjunto_3)

#aplica un metodo
conjunto_2.update(conjunto_1) #actualizacion de datos
#print(conjunto_2)

conjunto_2.clear() #eliminacion de datos
#print(conjunto_2)

'''
tuplas 
son estructuras en python mas rigidas,
son inmutables,
almacenan distintos tipos de datos
'''
tupla_1=(1,1,1,1,1,1,1,1,"b",True)
print(type(tupla_1))
print(tupla_1.count("b"))

print(tupla_1.index("b"))


