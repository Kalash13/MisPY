def calcular_vuelto(monto, respuesta):
    if monto < respuesta:
        print("Dinero insuficiente")
    else:
        resultado = (monto - respuesta )
        print(f"Su vuelto es : {resultado}")


print("Elija los productos que llevara 👌")
print("CATALOGO DE PRODUCTOS: \n-Agua $600 \n-Azucar $1200 \n-Aceite $1500 \n-Arroz $1250 \n-Fideos $790 \n-Bebida $1780 \n-Chocolate $2500 \n-Panmolde $1340 " )
precio =  0
p = 0



p1 = input ("Agua: si/no :  ")
if p1 == "si":
    precio = (precio + 600)
    p = (p + 1)
    print ("Producto añadido")
elif p1 == "no":
    print("Siguiente producto")

p2 = input ("Azucar: si/no :  ")
if p2 == "si":
    precio = (precio + 1200)
    p = (p + 1)
    print ("Producto añadido")
elif p2 == "no":
    print("Siguiente producto")

p3 = input ("Aceite: si/no :  ")
if p3 == "si":
    precio = (precio + 1500)
    p = (p + 1)
    print ("Producto añadido")
elif p3 == "no":
    print("Siguiente producto")

p4 = input ("Arroz: si/no :  ")
if p4 == "si":
    precio = (precio + 1250)
    p = (p + 1)
    print ("Producto añadido")
elif p4 == "no":
    print("Siguiente producto")

p5 = input ("Fideos: si/no :  ")
if p5 == "si":
    precio = (precio + 790)
    p = (p + 1)
    print ("Producto añadido")
elif p5 == "no":
    print("Siguiente producto")

p1 = input ("Bebida: si/no :  ")
if p1 == "si":
    precio = (precio + 1780)
    p = (p + 1)
    print ("Producto añadido")
elif p1 == "no":
    print("Siguiente producto")

p1 = input ("Chocolate: si/no :  ")
if p1 == "si":
    precio = (precio + 2500)
    p = (p + 1)
    print ("Producto añadido")
elif p1 == "no":
    print("Siguiente producto")

p1 = input ("Panmolde: si/no :  ")
if p1 == "si":
    precio = (precio + 1340)
    p = (p + 1)
    print ("Producto añadido")
elif p1 == "no":
    print("Siguiente producto")

print(f"Cantidad de productos: {p}  Total a pagar:$ {precio} ")

cliente = input("¿Usted es socio? : si/no: ")
if cliente == "si":
    mul = (precio * 0.25)
    res = (precio - mul)
    print(f"Descuento 25% aplicado, total a pagar: {res}")
    pago = int(input("Ingrese con cuanto cancela: "))
    calcular_vuelto(pago, res)




elif cliente == "no":
    print(f"No se aplica descuento, total a pagar: ${precio}")
    pago = int(input("Ingrese con cuanto cancela: "))
    pago = (pago - precio)
    print(f"Su vuelto es : {pago}")











