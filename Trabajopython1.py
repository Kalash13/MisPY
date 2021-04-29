"""
Trabajo de python 

En el trabajo los sistemas pedidos vienen con su titulo,
para ejecutarlo descomente el codigo  

"""




"""Validacion de edad"""
# edad = int (input ("Ingrese su edad:  "))

# if edad >= 18: 
#     print("Es mayor de edad ")

# else:
#     print("Usted es menor de edad")

"""Validacion de usuario y contraseña"""

# access = False
# user = input( " Ingrese su user : " )
# password = input( " Ingrese su password : " )
# if user == "pedro" and password == "123":
#     access = True

# if user == "angel" and password == "a4s1" :
#     access = True

# if access:
#     print( f" Bienvenido {user}")

# else:
#     print("Usuario no permitido")


"""Esto es para sacar el promedio"""
# print ("Ingrese sus notas para obtener su promedio!!!")
# nota1 = float  (input("Ingrese primera nota: "))
# nota2 = float (input("Ingrese segunda nota: "))
# nota3 = float  (input("Ingrse tercera nota: "))
# promedio = (nota1+nota2+nota3)/3
# if promedio >= 4:
#     print(f"Su promedio es: {promedio:.1f} Felicidades aprobo el ramo " )

# else: 
    # print("Usted reprobo el Ramo ")

"""Esto es pregunta con puntaje"""

# print("¿Cuál de los siguientes animales vive en el agua?")
# animals= ["1. perro", "2. cocodrilo", "3. conejo" , "4. tiburón"]
# for x in animals:
#     print(x)


# respuesta = int (input("Ingrese su respuesta con el numero asignado al animal: "))
# points = 0

# if respuesta == 2:
#     points = points + 0.5
#     print("Casi correcto, pero estos animales son semi acuaticos,  no viven en el agua pero si pasan gran parte de su dia en ella")

# elif respuesta == 4:
#     points = points + 1
#     print("Excelente tu respuesta es correcta :D ")
# else:
#     print("Intente nuevamente")

# print(f"Su puntaje es de : {points} ")

"""Esto es un juego de pregunta """
print("Bienvenido a la trivia de cine ")
print("Esta trvia consta de 3 preguntas con 10pts c/u , con una exigencia del 60 porc segun su puntaje se le asgina una nota ")
print("¿Quien es el director de la pelicula Taxi Driver ?")
director= ["a - Quentin Tarantino", "b - Clit Eastwood", "c - Martin Scorsese" , "d - David Lynch"]
for x in director:
    print(x)

respuesta1 = input("Ingrese su respuesta mediante la letra que corresponda: ")
points = 0

if respuesta1 == "c":
    print("Respuesta correcta ")
    points = (points + 10)


else: 
    print("Respuesta incorrecta")


print("¿Quien es el actor principal de la isla siniestra ?")
director= ["a - Leonardo DiCaprio", "b - Matt Damon", "c - Ben Kinglsey" , "d - Mark Ruffalo"]
for x in director:
    print(x)

respuesta2 = input("Ingrese su respuesta mediante la letra que corresponda: ")


if respuesta2 == "a":
    print("Respuesta correcta ")
    points = (points + 10)


else: 
    print("Respuesta incorrecta")


print("¿Cual es el nombre de la segunda pelicula en estrnarse de star wars ?")
director= ["a - La amenaza fantasma", "b - La venganza de los sith", "c - El retorno del  jedi" , "d - El imperio contraataca"]
for x in director:
    print(x)

respuesta3 = input("Ingrese su respuesta mediante la letra que corresponda: ")


if respuesta3 == "d":
    print("Respuesta correcta ")
    points = (points + 10)


else: 
    print("Respuesta incorrecta")

nota = 0
if points == 30:
    nota = 7.0 

if points == 20:
    nota = 4.5

if points == 10: 
    nota = 2.7

elif points == 0:
    nota = 1.0
print(f" Su puntaje es : {points} y su nota es : {nota}" )













