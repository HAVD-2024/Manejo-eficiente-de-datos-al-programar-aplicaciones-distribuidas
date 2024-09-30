import pandas as pd

# Cargar el archivo CSV
csv_file = '/data/airlines/2024_3 - copia.csv'
df = pd.read_csv(csv_file, low_memory=False)

# Filtrar las filas con la columna de retraso de llegada ('ArrDelay')
df['OnTime'] = df['ArrDelay'].apply(lambda x: 1 if x <= 0 else 0)

# Agrupar por 'Reporting_Airline' y calcular el porcentaje de vuelos a tiempo
on_time_percentage = df.groupby('Reporting_Airline').agg(
    Total_Flights=('OnTime', 'size'),
    OnTime_Flights=('OnTime', 'sum')
).reset_index()

on_time_percentage['OnTime_Percentage'] = (
    on_time_percentage['OnTime_Flights'] / on_time_percentage['Total_Flights']
) * 100

# Ordenar por el porcentaje de vuelos a tiempo en orden descendente
top_10_airlines = on_time_percentage.sort_values(by='OnTime_Percentage', ascending=False).head(10)

# Mostrar el resultado
print("Top 10 aerolíneas con mayor efectividad de llegada a tiempo:")
print(top_10_airlines[['Reporting_Airline', 'OnTime_Percentage']])