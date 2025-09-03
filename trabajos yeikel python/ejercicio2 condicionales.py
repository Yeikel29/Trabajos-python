saldo = "300"
retiro = "320"
monto = input("ingrese el monto del retiro")



if saldo < monto :
    print("usted no tiene suficientes fondos")

elif saldo > monto :
    print("Su retiro se puede realizar")
