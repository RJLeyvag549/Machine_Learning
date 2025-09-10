import pandas as pd

# Lista con los datos
personas = [
    {"Nombre": "Ana", "Edad": 23, "Estado": "Activo"},
    {"Nombre": "Luis", "Edad": 30, "Estado": "Inactivo"},
    {"Nombre": "Carla", "Edad": 19, "Estado": "Activo"},
    {"Nombre": "Pedro", "Edad": 27, "Estado": "Activo"}
]

# Convertir la lista a un DataFrame
df = pd.DataFrame(personas)

# Mostrar la tabla
print(df)
print(df.loc[df["Estado"] == "Activo"])