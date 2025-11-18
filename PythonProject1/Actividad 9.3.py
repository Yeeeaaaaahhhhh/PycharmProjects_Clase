'''presentarse(): imprime una presentación básica.
es_mayor_de_edad(): retorna True o False.
Agrega una clase hija que será Profesor
Agrega los atributos materia y anios_experiencia
Los métodos deberá ser ensenarque  imprime qué materia enseña además el método evaluar que  imprime un mensaje de evaluación.
En el tercer nivel de la jerarquía Nieto: ProfesorTutor será hija de Profesor
El atributo correspondientes es grupo_tutorado
con los métodos orientar_estudiantesque solo imprima un mensaje de orientación.
y mostrar_información que muestra toda la información del tutor.
Estudiante será hija de persona
Atributos serán grado y promedio
Debes implementar los métodos estudiar que imprime un mensaje de qué esta estudiando
También el método aprobar que deberá  indica si aprueba con base en el promedio.
Ahora creamos un nieto EstudianteBecado que será hijo de Estudiante
el atributo será tipo_beca
Los métodos a desarrollar son
mostrar_beca  que imprime qué beca tiene
renovar_beca() simula la renovación de beca.
Solamente genera la instancia de la clase
 ProfesorTutor
 EstudianteBecado
Para llamar los métodos'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def esmayordeedad(self):
        self.mayor = False
        if self.edad >= 18:
            self.mayor = True
        else:
            self.mayor = False
        if self.mayor is True:
            return ("Soy adulto")
        else:
            return ("Soy un bebito")

    def presentarse(self):
        print(f'''Hola! Soy {self.nombre} y me gusta jugar futbol y jugar con mis amigos
Tengo {self.edad} anitos y me gusta mucho paw patrol porque {self.esmayordeedad()}''')

class Profesor(Persona):
    def __init__(self, nombre, edad,materia,anos):
        super().__init__(nombre, edad)
        self.materia = materia
        self.anos = anos
    def ImprimirProfesor(self):
        print(f'''Hola! Soy {self.nombre} y me gusta jugar futbol y jugar con mis amigos
Tengo {self.edad} anitos y me gusta mucho paw patrol porque {self.esmayordeedad()}. He enseñado {self.materia}
por {self.anos} años.''')

class ProfesorTutor(Profesor):
    def __init__(self, nombre, edad,materia,anos, grupo):
        super().__init__(nombre, edad,materia,anos)
        self.grupo = grupo
    def grupo_tutorado(self):
        print("Vamonos por unas miches chicos la escuela es para perdedores")
    def imprimirProfesorTutor(self):
        print(f'''Hola! Soy {self.nombre} y me gusta jugar futbol y jugar con mis amigos
Tengo {self.edad} anitos y me gusta mucho paw patrol porque {self.esmayordeedad()}. He enseñado {self.materia}
por {self.anos} años. Soy tutor del grupo de {self.grupo}''')

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado,promedio):
        super().__init__(nombre, edad)
        self.grado = grado
        self.promedio = promedio
    def Estudiar(self):
        print("Estoy 'estudiando'")
    def Aprobador(self):
        aprobado = False
        if self.promedio >= 60:
            aprobado = True
        else:
            aprobado = False
        if self.promedio is True:
            return ("Soy un mal estudiante y debo de dejar de pistear tanto y estudiar")
        else:
            return ("Soy un buen estudiante y necesito pistear mas")
    def ImprimirEstudiante(self):
        print(f'''Hola! Soy {self.nombre} y me gusta jugar futbol y jugar con mis amigos
Tengo {self.edad} anitos y me gusta mucho paw patrol porque {self.esmayordeedad()}. Voy en {self.grado} grado
y {self.promedio}.''')

class EstudianteBecado(Estudiante):
    def __init__(self, nombre, edad,grado,promedio,beca):
        super().__init__(nombre, edad,grado,promedio)
        self.beca = beca
    def MostrarBeca(self):
        print(f"Tengo {self.beca} de beca")
    def RenovarBeca(self):
        becaRenovada = str("Quieres renovar tu beca?(S o N): ")
        if becaRenovada == "S":
            print("Beca renovada con exito")

        elif becaRenovada == "N":
            print("Beca no renovada tonto")
            self.beca = 0

        else:
            print("Elige una opcion valida")

    def ImprimirEstudianteBecado(self):
        print(f'''Hola! Soy {self.nombre} y me gusta jugar futbol y jugar con mis amigos
Tengo {self.edad} anitos y me gusta mucho paw patrol porque {self.esmayordeedad()}. Voy en {self.grado} grado
y {self.promedio}. Tengo beca del {self.beca}''')






#Persona
nombre1 = str(input("Cual es tu nombre? "))
edad1 = int(input("Cuantos anos tienes? "))
persona = Persona(nombre1,edad1)
persona.esmayordeedad()
persona.presentarse()

#EstudianteBecado
grado1 = int(input("En que grado vas? "))
promedio1 = int(input("Cual es tu promedio? "))
beca1 = int(input("Cual es tu porcentaje de beca? "))
estudiante = EstudianteBecado(nombre1,edad1,grado1,promedio1,beca1)
estudiante.MostrarBeca()
estudiante.RenovarBeca()
estudiante.ImprimirEstudianteBecado()
#profesor tutor

anos1 = int(input("Cuantos anos tienes esneñando?: "))
materia1 = str(input("Cual es la materia que enseñas?: "))
grupo1 = str(input("Que grupo tutoras?: "))
profesortutor = ProfesorTutor(nombre1,edad1,materia1,anos1,grupo1)
profesortutor.grupo_tutorado()
profesortutor.imprimirProfesorTutor()





