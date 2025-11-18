from random import*

dado1 = 0
dado2 = 0
def lanzar_dados():
    dado1 = randint(1,7)
    dado2 = randint(1,7)
    suma = dado1 + dado2
    print(dado1,dado2)
    if suma <= 6:
        return (f"La suma de tus dados es {suma}... Lamentable")
    if suma < 10:

        return (f"la suma de tus dados es {suma}. Tienes buenas chances")
    else:

        return (f"La suma de tus dados es {suma}. Parece una jugada ganadora")

lista_1 = [1,5,-9,98,101,46,-22,-88]

def pares():
    cuenta_pares = 0
    for i in lista_1:
        if i % 2 == 0:
            cuenta_pares += 1
    return(cuenta_pares)

def suma_menores ():
    sumas = 0
    for i in lista_1:
        if i > 0 and i < 100:
            sumas += i
        else:
            sumas +=0
    return(sumas)

def todos_positivos():
    lista_neg = []
    lista_pos = []
    for i in lista_1:
        if i >= 0:
            lista_pos.append(i)

        else:
            lista_neg.append(i)
    return(f"La lista negativa es {lista_neg}, la lista positiva es {lista_pos}")


opcion = int(input("Selecciona un numero del 1 al 4: "))
if opcion == 1:
    print(lanzar_dados())
if opcion ==2:
    print(pares())
if opcion ==3:
    print(suma_menores())
if opcion ==4:
    print(todos_positivos())



