
import sys

def reducer():
    """Función reducer que suma el conteo de vuelos por ID de aeropuerto."""
    current_airport_id = None
    total_flights = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        airport_id, count = line.split("\t")
        count = int(count)

        if current_airport_id == airport_id:
            total_flights += count
        else:
            if current_airport_id is not None:
                # Imprimir el resultado para el aeropuerto anterior
                print(f"{current_airport_id}\t{total_flights}")
            current_airport_id = airport_id
            total_flights = count

    # Imprimir el resultado para el último aeropuerto
    if current_airport_id is not None:
        print(f"{current_airport_id}\t{total_flights}")

if __name__ == "__main__":
    reducer()
