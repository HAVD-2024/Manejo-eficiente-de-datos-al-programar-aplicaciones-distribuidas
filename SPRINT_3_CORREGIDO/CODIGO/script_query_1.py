import pandas as pd

# Cargar el archivo CSV con el argumento low_memory=False para evitar el DtypeWarning
csv_file = '/data/airlines/2024_3 - copia.csv'

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file, low_memory=False)

# Agrupar por la columna 'Reporting_Airline' y contar el número de vuelos
top_airlines = df.groupby('Reporting_Airline').size().reset_index(name='Total_Flights')

# Ordenar por el número de vuelos en orden descendente
top_airlines = top_airlines.sort_values(by='Total_Flights', ascending=False)

# Seleccionar el top 5 de aerolíneas con más vuelos
top_5_airlines = top_airlines.head(5)

# Mostrar el resultado
print("Top 5 aerolíneas con más vuelos:")
print(top_5_airlines)