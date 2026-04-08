

import random


lista = []
for random_number in range(101):
    lista.append(random.randint(100, 200))

print(lista)

indice = 0

mayor = lista[0]
while indice < 99:
    if mayor < lista[indice + 1]:
        mayor = lista[indice + 1]
    indice += 1

print(f"el numero mas grande es {mayor}")
menor = lista[0]
while indice < 99:
    if menor > lista[indice + 1]:
        menor = lista[indice + 1]
    indice += 1

print(f"el numero mas pequeño es {menor}")