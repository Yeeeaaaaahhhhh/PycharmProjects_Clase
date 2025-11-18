lista_numeros = [4,3,5,6,7,9,10,13]
lista_letras = ["ola soy pablito"]
cubo = list(map(lambda x: x**3, lista_numeros))
print(cubo)

mayus = list(map((lambda x: x.capitalize()), lista_letras))
print(mayus)

longitud = list(map(lambda x: len(x), lista_letras))
print(longitud)

lista_numeros2= [3,4,5,6,7,8,9]
suma = list(map(lambda x,y: x+y, lista_numeros , lista_numeros2))
print(suma)

clasificar = list(map(lambda x: x%2==0, lista_numeros))
clasificar1 = list(map(lambda x: x%2!=0, lista_numeros))
print(clasificar, "par")
print(clasificar1, "impar")

lista_numeros3 = [10,-3,-5,8,0,-1,4]
negativos = list(map(lambda x: x* -1, lista_numeros3))
print(negativos)

mult5 = list(map(lambda x: x%5==0, lista_numeros))
print(mult5,"multiplos de 5")

num5y10 = list(map(lambda x:5>x<10, lista_numeros))
print(num5y10)

lista_numeros4 = [-5,0,10,15,20,-2,5]
promedio = lista_numeros4.count(0)/len(lista_numeros4)
ponderaicion = list(map(lambda x: x/promedio, lista_numeros4))
print(ponderaicion)
