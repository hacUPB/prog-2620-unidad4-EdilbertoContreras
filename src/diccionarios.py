# Diccionario vacío
aeronave = {}

# Diccionario con elementos
aeronave = {
    "modelo": "Boeing 787-9",
    "envergadura": 60.17,  # metros
    "longitud": 62.81,     # metros
    "mtow": 254000,        # kg
    "velocidad_max": 954   # km/h
}

# Diccionario con diferentes tipos de datos como valores
vuelo = {
    "numero": "AA123",
    "origen": "KLAX",
    "destino": "KJFK",
    "distancia": 3983,
    "a_tiempo": True,
    "tripulacion": ["Capitán Smith", "F/O Johnson", "F/E Williams"]
}

# Creación con dict()
motor = dict(fabricante="GE", modelo="GE9X", empuje=470, bypass_ratio=10)
print(vuelo ["tripulacion"])  # Imprime el nombre del capitán
print(motor["fabricante"])      # Imprime el fabricante del motor

vuelo["a_tiempo"] = False  # Actualiza el valor de "a_tiempo"
print(vuelo["a_tiempo"])  # Imprime el nuevo valor de "a_tiempo"

del vuelo["distancia"]  # Elimina la clave "distancia" y su valor
print(vuelo)  # Imprime el diccionario vuelo sin la clave "distancia"   
print(vuelo.get("distancia", "Clave no encontrada"))  # Imprime un mensaje si la clave "distancia" no existe