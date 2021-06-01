# Esto es el juego del ahorcado
# nombre=input("Ingresa tu Nombre:  ")
# print("Hola "+nombre,", Este es el juego del ahorcado")
# print("Comienza a adivinar")


# p = "CALENDARIO"
# p = p.lower()

# x = len("CALENDARIO")
# print("La palabra tiene",x , "Caracteres ")
# up=" "

# v=2
# while v > 0:
#     errors = 0
#     for letra in p:
#         if letra in up:
#             print(letra,end="")
#         else:
#             print(".",end="")
#             errors+=1
#     if errors ==0:

#         print("")
#         print("¡Felicidades! ")
#         print("¡GANASTE!")
#         print("")
#         break

#     letra=input(" |Ingrese letra: ")
#     up+=letra

#     if letra not in p:
#         v-=1
#         print("Error")
#         print("Te quedan ",+v," oportunidad")
#     if v== 0:
#         print("Perdiste!")
# else:
#     print("gracias por participar")



# Esto es la pizzeria

def calcular_vuelto(monto, respuesta):
    if monto < respuesta:
        print("Dinero insuficiente")
    else:
        resultado = (monto - respuesta )
        print(f"Su vuelto es : {resultado}")


pt= 12000
pp= 14000
ptc = 16000
opcion = 0
contador = 0
while opcion != 4:
    print ("Bienvenido a PizzaDuc")
    print ("1- Menú")
    print ("2- Pagar")
    print ("3- Anular pedido")
    print ("4- Exit")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("Pizzas: \n-Tradicional $12.000 \n-Pepperoni $14.000 \n-Todas las carnes $16.000")
        pizza = input("Seleccion tus pizzas: ")
        if pizza == "tradicional":
            cantidad = int(input("Seleccione cantidad: "))
            contador= contador + pt *cantidad
        if pizza == "pepperoni":
            cantidad = int(input("Seleccione cantidad: "))
            contador= contador + pp *cantidad
        if pizza == "todas las carnes":
            cantidad = int(input("Seleccione cantidad: "))
            contador= contador + ptc *cantidad

        total = contador

    if opcion == 2 and True:
        conv = input("Usted es estudiante diurno ?  s / n : ")

        if conv == "s":
            convenio = True
        if conv == "n":
            convenio = False

        if conv == "s":
            mul = (total * 0.12)
            res = (total - mul)
            print("")
            print("PizzaDuc")
            print("--------------------")
            print(f" {cantidad}  {pizza}  :  {contador}  " )

            print("---------------------")
            print(f"Subtotal: {total}")
            print(f"Descuento: {mul} ")
            print("----------------------")



            pago =int(input("Ingrese con cuanto va a pagar: "))
            calcular_vuelto (pago , res)
            break

        elif  conv == "n":
            print("")
            print("PizzaDuc")
            print("---------------------")
            print(f" {cantidad}  {pizza}  :  {contador}  " )

            print("---------------------")
            print(f"Subtotal: {total}")
            print("Descuento: 0 ")
            print("----------------------")
            print(f"Total: {total}")
            print("----------------------")
            pago = int(input("Ingrese con cuanto cancela: "))
            calcular_vuelto(pago ,total)
            break



    if opcion == 3:
        print("Se anulado la compra o no hay productos agregados")



    if opcion == 4:
        break