
saldo = 100

nip = int(input("DIGITA TU NIP: "))

while nip == 5652:
    print("..................................")
    print("::::::: CAJERO AUTOMÁTICO ::::::::")
    print("..................................")
    print("\n > CONSULTAR SALDO ......... [1]")
    print("\n > RETIRAR ................. [2]")
    print("\n > DEPOSTAR ................ [3]")
    print("\n > SALIR ................... [4]")

    numero = int(input("\n¿QUE DESEAS REALIZAR? "))

    while numero != 4:

        if numero == 1:
            print("...................................")
            print(":::::::: CONSULTA DE SALDO ::::::::")
            print("...................................")
            print(f" >> TU SALDO ACTUAL ES DE ${saldo}")
            print("...................................")
        elif numero == 2:
            print("...................................")
            print("::::::::: RETIRO DE SALDO :::::::::")
            print("...................................")
            retiro = float(input(" > CANTIDAD A RETIRAR: "))

            if saldo > retiro:
                saldo = saldo - retiro
                print(f" >> TU SALDO ACTUAL ES DE ${saldo}")
                print("...................................")
            else:
                print("<< NO TIENES SALDO SUFICIENTE >>")
                print("................................")
        elif numero == 3:
            print("...................................")
            print(":::::::: DEPOSITO DE SALDO ::::::::")
            print("...................................")
            deposito = float(input(" > CANTIDAD A DEPOSITAR: "))

            if saldo <= 100000:
                saldo = saldo + deposito
                print(f" >> TU SALDO ACTUAL ES DE ${saldo}")
                print("...................................")
            else:
                print(" << LIMITE DE SALDO EXCEDIDO >>")
                print("...............................")
        else:
            print("...................................")
            print("    << OPERACIÓN INEXISTENTE >>    ")
            print("...................................")

        print("\n > CONSULTAR SALDO ......... [1]")
        print("\n > RETIRAR ................. [2]")
        print("\n > DEPOSTAR ................ [3]")
        print("\n > SALIR ................... [4]")

        numero = int(input("\n¿QUE DESEAS REALIZAR?"))
    else:
        print(".......................................")
        print("::: GRACIAS, FUE UN GUSTO ATENDERTE :::")
        print(".......................................")

        nip = int(input("DIGITA TU NIP: "))
else:
     print("...................................")
     print("    << NIP INCORRECTO >>    ")
     print("...................................")



