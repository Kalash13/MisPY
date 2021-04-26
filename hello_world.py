

#ejemplo pasaje/diferido

categoria = input( "Ingrese 'Tercera', 'Escolar' o 'General': " )
pasaje = 0

if categoria == "Tercera":
    pasaje = 100
    print ("valor a pagar: " + str(pasaje) )
elif categoria == "Escolar":
    pasaje = 50
    print ("valor a pagar: " + str(pasaje) )
else: 
    pasaje = 500
    print ("valor a pagar: " + str(pasaje) )
