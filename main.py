import funciones as llamar

while True:
    print("\n </> ---- Menú de Opciones ---- </> \n")
    print("1. Registrar Trabajador\n2. Listar los todos los trabajadores\n3. Imprimir planilla de sueldos\n4. Salir del programa\n")
    try:
        opcion = int(input("Ingrese una opción del 1 al 4 ---> "))
    except:
        print("Dato ingresado no válido... Intentalo de Nuevo...")
    else:
        if opcion == 1:
            llamar.registrar_trabajador()
        elif opcion == 2:
            llamar.mostrarr()
        elif opcion == 3:
            print("Disculpe profe, no nos dió pa ma'")
        elif opcion == 4:
            llamar.salir()
            print("Disculpe profe, no nos dió pa ma'")
        else:
            print("Opción no válida... Vuelva a intentarlo...")

