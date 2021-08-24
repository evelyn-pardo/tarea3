menu = 0
while menu<4:
    print("Ingresar una opcion")
    print("1 para pila")
    print("2 para cola")
    print("3 para lista")
    print("4 para Salir")
    menu = float(input())
    if menu==1:
        print("Aqui se hará la pila")
    elif menu==2:
        print("Aqui se hará la cola")
    elif menu==3:
        print("Aqui se hará la lista")
    elif menu==4:
        print("Gracias por visitarnos")
    else:
        print("Opción no valida")
    input()
    print("")