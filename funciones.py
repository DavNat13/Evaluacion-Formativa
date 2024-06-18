#Definir funciones: 
trabajadores = []


def registrar_trabajador():
    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador: ")
    try:

        sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
    except:
        print("Dato no válido...")
    # Cálculo de descuentos y sueldo líquido
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    sueldo_liquido = sueldo_bruto - desc_salud - desc_afp

    trabajador = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Cargo": cargo,
        "Sueldo Bruto": sueldo_bruto,
        "Desc. Salud": desc_salud,
        "Desc. AFP": desc_afp,
        "Líquido a pagar": sueldo_liquido
    }
    with open("trabajadores.txt", "a", encoding='utf-8') as archivo:
        archivo.write("Nombre\t Apellido\tCargo \tSueldo Bruto \tDesc. Salud \tDesc. AFP \tLíquido a pagar\n")
        archivo.write(f"{nombre}\t{apellido} \t{cargo}\t {sueldo_bruto} \t {desc_salud}\t{desc_afp} \t{sueldo_liquido}\n")
        archivo.write("\n")
    trabajadores.append(trabajador)
    print("Trabajador registrado exitosamente.\n")  

def mostrarr():
    print(trabajadores)

def salir():
    print("Saliendo del programa...")
    exit()

'''def listarT():
    pedirC = input("Ingrese un cargo para buscar: ")
    if pedirC in cargos:
        print(baseD)
    else:
        print("No se ha encontrado es cargo...")'''