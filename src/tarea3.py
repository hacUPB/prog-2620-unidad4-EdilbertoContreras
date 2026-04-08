filas = int(input("Ingrese número de filas: "))
columnas = int(input("Ingrese número de columnas: ")) 
temperatura = []
print("Ingrese los elementos de la matriz temperatura:")

for i in range(filas):
    fila = list(map(int, input(f"Ingrese temperatura ciudad {i + 1} (separada por espacios): ").split()))
    
    if len(fila) != columnas:
        print("Número de columnas incorrecto")
        break   
    temperatura.append(fila)

print("Matriz temperatura:")
for fila in temperatura:
    print(fila)

for i, ciudad in enumerate(temperatura):
    promedio = sum(ciudad) / len(ciudad)
    print(f"Ciudad {i + 1}: {promedio}")