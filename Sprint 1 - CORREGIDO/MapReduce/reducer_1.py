import sys

def main():
    """Función principal del reducer que suma el conteo de vuelos por día."""
    current_day = None
    total_flights = 0

    for line in sys.stdin:
        line = line.strip()
        day_of_month, count = line.split('\t')
        count = int(count)

        if current_day == day_of_month:
            total_flights += count
        else:
            if current_day is not None:
                print(f"{current_day}\t{total_flights}")
            current_day = day_of_month
            total_flights = count

    if current_day is not None:
        print(f"{current_day}\t{total_flights}")

if __name__ == "__main__":
    main()
