# Lista principal
flota = []

# Número de aeronaves
num_aeronaves = int(input("Ingrese la cantidad de aeronaves (mínimo 3): "))

# Registro de aeronaves
for i in range(num_aeronaves):
    print("\nAeronave", i + 1)

    matricula = input("Matrícula: ")
    modelo = input("Modelo: ")
    horas_vuelo = float(input("Horas de vuelo: "))

    # Lista de componentes
    componentes = []

    num_componentes = int(input("Número de componentes: "))

    for j in range(num_componentes):
        print("  Componente", j + 1)

        nombre = input("  Nombre: ")
        horas_uso = float(input("  Horas de uso: "))
        limite = float(input("  Límite de horas: "))

        componente = {
            "nombre": nombre,
            "horas_uso": horas_uso,
            "limite": limite
        }

        componentes.append(componente)

    # Diccionario de aeronave
    aeronave = {
        "matricula": matricula,
        "modelo": modelo,
        "horas_vuelo": horas_vuelo,
        "componentes": componentes
    }

    flota.append(aeronave)

#  REPORTE DE MANTENIMIENTO
print("\n--- REPORTE DE MANTENIMIENTO ---")

for aeronave in flota:
    for componente in aeronave["componentes"]:
        if componente["horas_uso"] > componente["limite"]:
            print("\n Mantenimiento requerido")
            print("Aeronave:", aeronave["matricula"])
            print("Modelo:", aeronave["modelo"])
            print("Componente:", componente["nombre"])
            print("Horas:", componente["horas_uso"])
            print("Límite:", componente["limite"])
        else:
            print("\n Componente en buen estado")
            print("Aeronave:", aeronave["matricula"])
            print("Modelo:", aeronave["modelo"])
            print("Componente:", componente["nombre"])
            print("Horas:", componente["horas_uso"])
            print("Límite:", componente["limite"])