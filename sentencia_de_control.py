x=520
y=60

'''
condicional if elif else
if them else

if condicion>:
operacion 1
operacion 2
.
.
.
operacion n

'''
#caso1
if x > y: #condicion
    print("x es mayor que y") #operacion


 #caso2 ---> if else
if x > y: #condicion
    print("x es mayor que y")
else:
    print("x es mayor que y") 

#caso3 ---> uso de if elif else
if x > y: 
    print("x es mayor que y")
elif x == y: #condicion
    print("x es igual a y")
elif x/y==8: #condicion
    print("x dividido y es igual a 8 ")
else: # de lo contrario
    print("x es mayor que y") 


#variante 1
if x % 2 == 0 and x>500: # multiples condiciones a evaluar
    print("x es par y es mayor que 500")
# caso de login a aplicacion
usuario=input("por favor ingrese usuario")
password=input("por favor ingrese su password")
#if usuario=="alejandro" and password=="1234":
 #   print("usuario puede ingresar")
#else:
 #   print("usuario o contraseña incorrecta")

#print("ejecucion terminada")   
if usuario=="alejandro":
    password=input("por favor ingrese su password:")
    if password== "1234":
        print("usuario lo puede ingresar")
    else:
        print("contraseña incorrecta")
else:
    print("usuario incorrecto")
print("ejecucion terminada")