import pandas as pd

# Especificar la ruta del archivo
csv_file = '/data/airlines/2024_3 - copia.csv'

# Cargar los datos desde el archivo CSV
df = pd.read_csv(csv_file, low_memory=False)

# Verificar las primeras filas del DataFrame
print(df.head())

# Filtrar los datos para un rango de fechas específico (opcional)
df['FlightDate'] = pd.to_datetime(df['FlightDate'])
df = df[(df['FlightDate'] >= '2024-03-01') & (df['FlightDate'] <= '2024-03-31')]

# Calcular la distribución de rendimiento de llegada
on_time = (df['ArrDelay'] <= 0).mean() * 100
air_carrier_delay = (df['CarrierDelay'] > 0).mean() * 100
weather_delay = (df['WeatherDelay'] > 0).mean() * 100
nas_delay = (df['NASDelay'] > 0).mean() * 100
security_delay = (df['SecurityDelay'] > 0).mean() * 100
aircraft_arriving_late = (df['LateAircraftDelay'] > 0).mean() * 100
cancelled = (df['Cancelled'] == 1).mean() * 100
diverted = (df['Diverted'] == 1).mean() * 100

# Crear un diccionario con los resultados
performance_distribution = {
    'On Time': on_time,
    'Air Carrier Delay': air_carrier_delay,
    'Weather Delay': weather_delay,
    'National Aviation System Delay': nas_delay,
    'Security Delay': security_delay,
    'Aircraft Arriving Late': aircraft_arriving_late,
    'Cancelled': cancelled,
    'Diverted': diverted
}

# Convertir el diccionario a un DataFrame para mejor visualización
performance_df = pd.DataFrame(performance_distribution, index=[0])

# Mostrar los resultados
print(performance_df)
