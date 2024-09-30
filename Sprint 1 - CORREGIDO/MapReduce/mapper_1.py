import sys

def main():
    """Función principal del mapper que procesa entradas de vuelos."""
    for line in sys.stdin:
        # Dividir la línea por comas
        fields = line.strip().split(',')

        # Ignorar la línea de encabezado
        if fields[0] == 'Year':
            continue

        # Extraer el día del mes
        day_of_month = fields[3]  # Columna "DayofMonth"

        # Emitir el día del mes con un conteo de 1
        print(f"{day_of_month}\t1")

if __name__ == "__main__":
    main()
