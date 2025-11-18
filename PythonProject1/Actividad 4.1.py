'''Investigación teórica
Investiga en fuentes confiables y anota la referencia bibliográfica
Explica brevemente en qué consisten los siguientes métodos de manipulación de strings:
(1.-count, partition, rpartition, strip, lstrip, rstrip, isdigit, isnumeric, isdecimal, isalnum, 11.-isspace)
Daun ejemplo de uso para cada método investigado, acompañado de una breve explicación de su funcionamiento.
Presenta tu trabajo de manera ordenada, clara y con tus propias palabras.
Aplicación Práctica

1.count
    -Explicacion : Cuenta cuantas veces aparece una palabra en un texto
    texto = "Hola me llamo pablo me gusta el chocolate y me quiero comer uno"
    Conteo = texto.count("me")
    print(Conteo)
    output : 3

2.partition
    -Explicacion: Separa la cadena donde se encuentra la palabra definida.
    Solo es la primera aparicion
    frase = "Nombre : Pablo Barriga
    resultado = frase.partition(": ")
    print(resultado)
    output : ('Nombre', ': ', 'Pablo Barrriga')

3.rpartition
    Explicacion: Lo mismo pero es la ultima palabra q tu seleccionas
    frase = "C:/Usuarios/Pablo/Documentos"
    resultado = frase.rpartition("/ ")
    print(resultado)
    output : ('C:/Usuarios/Pablo' , '/', Documentos")

4.strip
    Explicacion : Elimina los espacions u otros caracteres al incio y al final
    frase = "      Pablo Barriga       "
    resultado = frase.strip()
    print(resultado)
    output : ('Pablo Barriga')

5.lstrip
    Explicacion : Elimina los espcios solo al inicio
    frase = "       Pablo Barriga"
    resultado = frase.lstrip()
    print(resultado)
    output : ('Pablo Barriga')

6.rstrip
    Explicacion: Lo mismo pero los del final
    frase = "Pablo Barriga       "
    resultado = frase.rstrip()
    print(resultado)
    output : ('Pablo Barriga')

7.isdigit
    Explicacion: Verifica si todos los caracteres de la cadena son digitos del 0 al 9
    edad = 46
    print(edad.isdigit()))
    output : True

8.isnumeric
    Explicacion: Lo mismo pero con mas tipos numericos como fracciones
    numero = "1/5"
    print(numero.isnumeric()))
    output : True

9.isdecimal
    Explicacion: Lo mismo pero con decimales, es mas estricto que isnumeric
    numero = 1234
    print(numero.isdecimal()))
    output : True

10.isalnum
    Explicacion: Verifica si la cadena esta compuesta de solo letras y/o numeros sin espacios ni simbolos
    usuario = Pablo3332
    print(usuario.isalnum()))
    output : True

11.isspace
    Explicacion: Checa si la cadena tiene solo espacios en blanco. Espacios, tabs o saltos de linea
    espacio = "     \t\n"
    print(espacio.isspace()))
    output : True





Encuentra y muestra en pantalla qué carácter ocupa la quinta posición dentro de la palabra "computadora".
Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
             "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la misma frase:'''


palabra = "computadora"
Letra_1 = palabra[5]
print(f"la 5ta letra en computadora es: {Letra_1}")

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
palabra_1 = frase.index("práctica")
print(f"La palabra 'practica' esta en el indice: {palabra_1}")

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
palabra_2 = frase.rindex("práctica")
print(f"La palabra 'practica' esta en el indice: {palabra_2}")
