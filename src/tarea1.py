# Tarea 1: contador de pasos y sus día más activos
pasos = []
dia = 0
for i in range(7):
    paso = int(input(f"Ingrese el número de pasos para el día {i + 1}: "))
    pasos.append(paso)
max_pasos = max(pasos)

dia = pasos.index(max_pasos)

promedio_pasos = sum(pasos) / len(pasos)
if dia == 0:
    dia = "Lunes"
elif dia == 1:
    dia = "Martes"
elif dia == 2:
    dia = "Miércoles"
elif dia == 3:
    dia = "Jueves"
elif dia == 4:
    dia = "Viernes"
elif dia == 5:
    dia = "Sábado"  
elif dia == 6:
    dia = "Domingo"

print(f"Pasos registrados: {pasos}")
print(f"Día más activo: {dia} con {max_pasos} pasos")
print(f"Promedio de pasos: {promedio_pasos:.2f}") 