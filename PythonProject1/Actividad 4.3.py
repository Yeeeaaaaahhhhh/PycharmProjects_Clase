'''Crear un programa que reciba como entrada una cadena y un carácter.
El programa debe insertar el carácter entre cada letra de la cadena.
Ejemplo:
Entrada: cadena = "separar", carácter = ","
Salida: "s,e,p,a,r,a,r"
Verificación de palíndromos
Escribir un programa que reciba una palabra y determine si es un palíndromo.
Recordar que un palíndromo es una palabra, número o frase que se lee igual de izquierda a derecha que de derecha a izquierda.
Ejemplo:
Entrada: "reconocer"
Salida: "Es un palíndromo"
Entrega:
Subir el código de  programas con comentarios que expliquen su funcionamiento.'''


#1
#pregunta la cadena y el caracter
cadena_1 = str(input("Ingresa una cadena: "))
caracter_1 = str(input("Ingresa una caractere: "))
#inicializa la variable resultado como string
resultado = ""

#agarra la longitud de la cadena 1 y agrega las letras en el indice i
for i in range(len(cadena_1)):
    resultado += cadena_1[i]
    # si es menor que i la longitud de la cadena -1, agrega la coma
    if i < len(cadena_1)-1:
        resultado += caracter_1

print(resultado)
print(len(cadena_1))

palabra_1 = str(input("Ingresa una palabra: "))
#inicializa la variable como booleano
palindromo = True

#checa si las letras son iguales
for i in range(len(palabra_1)):
    if palabra_1[i] != palabra_1[len(palabra_1)-1-i]:
        #si no son iguales, se rompe el ciclo y se cambia la variable a false
        palindromo = False
        print("No es un palindromo")
        break

else:
    print("Es un palindromo")