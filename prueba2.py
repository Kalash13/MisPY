def calcular_vuelto(monto, respuesta):
    if monto < respuesta:
        print("Dinero insuficiente")
    else:
        resultado = (monto - respuesta )
        print(f"Su vuelto es : {resultado}")

conv = input("Ustede tiene convenio ?  si / no : ")

if conv == "si":
    convenio = True
if conv == "no":
    convenio = False


hq = 4000
hr = 4600
hi = 4700
pn = 1200
pg = 1500
bn = 1000
bg = 1500
jn = 2000


print ("Hambuerguesas: \n-Hamburguesa Queso $4000 \n-Hamburguesa Ranchera $4600 \n-Hambuerguesa Italiana $4700")

hamb = input("Seleccione tipo de hamburguesa y cantidad : ")

cont1 = 0
if hamb == "queso":
    cant = int(input("Ingrese cantidad : "))
    cont1 = cont1 + hq  *cant

if hamb == "ranchera":
    cant = int(input("Ingrese cantidad: "))
    cont1 = cont1 + hr  *cant

if hamb == "italiana":
    cant = int(input("Ingrese cantidad: "))
    cont1 = cont1 + hi  *cant


print ("Papas fritas : \n-Papas fritas Normales $1200 \n-Papas fritas Grandes $1500 ")
pf = input("Escoja papas fritas: ")
cont2 = 0
if  pf == "normales":
    cant = int(input("Ingrese cantidad: "))
    cont2 = cont2 + pn  *cant

if  pf == "grandes":
    cant = int(input("Ingrese cantidad: "))
    cont2 = cont2 + pn  *cant

print ("Bebidas : \n-Bebida Normal $1000 \n-Bebida Grande $1500 \n-Jugo Natural $2000")
bebida = input("Escoja tipo de bebida y cantidad: ")

cont3= 0
if bebida == "normal":
    cant = int(input("Ingrese cantidad: "))

    cont3 = cont3 + bn  *cant
if bebida == "grande":
    cant = int(input("Ingrese cantidad: "))
    cont3 = cont3 + bg  *cant

if bebida == "jugo":
    cant = int(input("Ingrese cantidad: " ))
    cont3 = cont3 + jn  *cant

total = cont1 + cont2 + cont3


if conv == "si":
    mul = (total * 0.12)
    res = (total - mul)
    print(f"Descuento 40% aplicado, total a pagar: {res}")
    pago =int(input("Ingrese con cuanto va a pagar: "))
    calcular_vuelto (pago , res)

elif  conv == "no":
    print(f"No se aplica descuento, total a pagar: ${total}")
    pago = int(input("Ingrese con cuanto cancela: "))
    calcular_vuelto(pago ,total)

