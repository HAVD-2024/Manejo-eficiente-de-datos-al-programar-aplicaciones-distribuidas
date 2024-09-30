import pandas as pd

# Cargar el archivo CSV
csv_file = '/data/airlines/2024_3 - copia.csv'
df = pd.read_csv(csv_file, low_memory=False)

# Agrupar por aerolínea y contar el número de vuelos
top_5_airlines = (
    df.groupby('Reporting_Airline')
    .size()
    .reset_index(name='Total_Flights')
    .sort_values(by='Total_Flights', ascending=False)
    .head(5)
)

# Filtrar el dataframe original para incluir solo las 5 aerolíneas con más vuelos
filtered_df = df[df['Reporting_Airline'].isin(top_5_airlines['Reporting_Airline'])]

# Calcular el tiempo promedio de demora en la llegada por aerolínea
avg_delay_by_airline = (
    filtered_df.groupby('Reporting_Airline')['ArrDelay']
    .mean()
    .reset_index(name='Avg_Arrival_Delay')
)

# Ordenar por el tiempo promedio de demora
avg_delay_by_airline = avg_delay_by_airline.sort_values(by='Avg_Arrival_Delay')

# Mostrar el resultado
print("Tiempo promedio de demora de las 5 aerolíneas con más vuelos:")
print(avg_delay_by_airline)