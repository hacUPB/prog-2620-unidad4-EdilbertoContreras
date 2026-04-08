# file: input_matriz.py

filas = int(input("Ingrese número de filas: "))
columnas = int(input("Ingrese número de columnas: "))

matrizA = []
print("Ingrese los elementos de la matriz A:")

for i in range(filas):
    fila = list(map(int, input(f"Ingrese fila {i} (separada por espacios): ").split()))
    
    if len(fila) != columnas:
        print("Número de columnas incorrecto")
        break   
    matrizA.append(fila)

matrizB = []
print("Ingrese los elementos de la matriz B:")

for i in range(filas):
    fila = list(map(int, input(f"Ingrese fila {i} (separada por espacios): ").split()))
    
    if len(fila) != columnas:
        print("Número de columnas incorrecto")
        break   
    matrizB.append(fila)

print("Matriz ingresada A:")
for fila in matrizA:
    print(fila)

print("Matriz ingresada B:")
for fila in matrizB:
    print(fila)

resultado = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(matrizA[i][j] + matrizB[i][j])
    resultado.append(fila)

print("Resultado de la suma:")
for fila in resultado:
    print(fila)