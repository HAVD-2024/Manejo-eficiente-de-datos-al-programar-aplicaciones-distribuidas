import pandas as pd

# Cargar el archivo CSV
csv_file = '/data/airlines/2024_3 - copia.csv'
df = pd.read_csv(csv_file)

# Filtrar filas donde 'DepDelay' no es nulo
df_filtered = df[df['DepDelay'].notnull()]

# Crear una nueva columna para la ruta
df_filtered['Route'] = df_filtered['Origin'] + ' - ' + df_filtered['Dest']

# Calcular la demora promedio por ruta
average_delay = df_filtered.groupby('Route')['DepDelay'].mean().reset_index()

# Ordenar por la demora promedio en orden descendente
top_delayed_routes = average_delay.sort_values(by='DepDelay', ascending=False).head(10)

# Mostrar el resultado
print(top_delayed_routes)