# ciclos para (for) - Mientras

# for i in range(4):
#     print('hola mundo')

# repeticiones = 10
# while (repeticiones > 0):
#     print('hola mundo')
#     repeticiones = repeticiones - 1


# opcion = ''
# while (opcion != 's'):
#     print('1) Sumar\n Restar\n  Salir )')
#     opcion = ('ingrese una opcion')
#     if opcion == '1':
#         a = int(input('Ingrese primer numero'))
#         b= int(input('Ingrese segundo numero'))
#         print('Resultado de suma = ',(a+b))


"""ESTA WEA SON LISTAS"""

# opcion = 0

# listaNombres = []

# listaRut = []



# while opcion != 4:

#     try:

#         if opcion == 1:

#             nombre = input( "Ingrese NOMBRE: " )

#             rut = input( "Ingrese RUT: ")



#             listaNombres.append( nombre )

#             listaRut.append( rut )



#         if opcion == 2:

#             nombre_busc = input( "BUSCAR = NOMBRE: " )

#             posicion = listaNombres.index( nombre_busc )

#             print("\tDATOS TRABAJADOR")

#             print(f" {listaNombres[posicion]} \t=> {listaRut[posicion]}")


#         if opcion == 3:

#             print(listaNombres)

#             print("====== LISTADO =====")

#             print("Numero de empleados: ",len(listaNombres))

#             for i in range( len(listaNombres)):

#                 print( "Nombre: ",listaNombres[i]," \t-> \t",listaRut[i])

#                 print("-------------------")





#         print("1) Ingresar Trabajador")

#         print("2) Ver Trabajador")

#         print("3) Ver Listado")

#         print("4) Salir")

#         opcion = int(input('Ingrese un opción: '))

#     except:

#         print("***** ERROR *****")



opcion = 0
usuario1 = True
usuario2 = True
usuario3 = True
contrasena1 = True
contrasena2= True
contrasena3 = True



while opcion != 3:

            if opcion == 1:
                user = input("Usuario: ")
                key = input("Contraseña: ")
                if user == usuario  and key == cont:

                    print(f"Bienvenido-->  {usuario}")
                    print("1) Realizar llamada")

                    print("2) Enviar correo")

                    print("3) Salir")

                    opcion = int(input('Ingrese un opción: '))


            if opcion == 2:
                usuario = input("Ingrese un usuario: ")
                cont = input("Ingrese un contraseña: ")
                
        


            print("1) Iniciar Sesión")

            print("2) Registrarse")

            print("3) Salir")

            opcion = int(input('Ingrese un opción: '))





