vuelo = {
    "aerolinea": "avianca",
    "vuelo": "AV123",
    "origen": "BOG",
    "destino": "MDE",
}

ciudad_llegada = vuelo["destino"]
print("Ciudad de llegada:", ciudad_llegada)

vuelo["destino"] = "CLO"
print("Nuevo destino:", vuelo["destino"])

vuelo["estado"] = "en el aire"
print(vuelo)

print(vuelo.get("piloto", "piloto no asignado"))

del vuelo["vuelo"]
print(vuelo)

print(vuelo["orige"])

