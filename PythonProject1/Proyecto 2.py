'''Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

La computadora  (el programa) jugará utilizando las 'X's
El usuario (Tu) jugarás utilizando las 'O's
El primer movimiento es de la maquina - siempre coloca una X en el centro del tablero.
Todos los cuadros están numerados comenzando con el 1
El usuario ingresa su movimiento introduciendo el número de cuadro elegido
El número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser
un cuadro que ya esté ocupado.
El programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el
juego continua, el juego termina en empate, tu ganas, o la computadora gana.
La computadora responde con su movimiento y se verifica el estado del juego

No se debe implementar algún tipo de inteligencia artificial
La maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

'''
import random
class Gato:

    def __init__(self):
        self.op_jugador = 11
        self.op_oponente = 11
    def oponente(self):
        eleccion_op1 = 11
        eleccion_op2 = 11
        eleccion_op3 = 11
        eleccion_op4 = 11
        eleccion_op5 = 11
        self.op_oponente = random.randint(0,8)
        while self.op_oponente == 5:
            self.op_oponente = random.randint(0,8)
        eleccion_op1 = self.op_oponente
        return(op_oponente)
    def cambiar_indice(self):
        posiciones[self.op_oponente] = "X"

"termina_juego = False"

gato = Gato()
"while termina_juego != True:"
posiciones = ["1","2","3","4","X","6","7","8","9"]

print(f''' .
|+-------+-------+-------+-------------+
|           |            |            |
|   {posiciones[0]}      |   {posiciones[1]}        |      {posiciones[2]}     |
|           |            |            |
|+-------+-------+-------+-------------
|           |             |           |
|   {posiciones[3]}       |   {posiciones[4]}         |   {posiciones[5]}       |
|           |             |           |
|+-------+-------+-------+|
|           |            |           |
|   {posiciones[6]}       |       {posiciones[7]}     |   {posiciones[8]}     |
|           |            |           |
|+-------+-------+-------+''')


print(gato.oponente())
gato.cambiar_indice()
