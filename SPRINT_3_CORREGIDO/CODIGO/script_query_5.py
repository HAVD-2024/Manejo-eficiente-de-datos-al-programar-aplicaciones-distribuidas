import pandas as pd

# Cargar el archivo CSV
csv_file = '/data/airlines/2024_3 - copia.csv'
df = pd.read_csv(csv_file, low_memory=False)

# Agrupar por aeropuerto de origen y contar el número de vuelos
top_airports = df.groupby('Origin').size().reset_index(name='Total_Flights')

# Ordenar por el número de vuelos en orden descendente
top_airports = top_airports.sort_values(by='Total_Flights', ascending=False)

# Mostrar los resultados
print("Aeropuertos con más vuelos de partida:")
print(top_airports)