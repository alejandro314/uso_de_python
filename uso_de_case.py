dia=input("ingrese el dia de la semana").lower()   #lower sirve para imprimir lo que escribas en minuscula e imprima
match dia:
    case "sabado"|"domingo":
        print(f"{dia} es fin de semana")
    case "lunes":
        print(f"{dia} es el dia mas dificil")
    case "martes" | "miercoles" | "jueves":
        print("es un dia normal")
    case _:
        print("el texto no es un dia de la semana")