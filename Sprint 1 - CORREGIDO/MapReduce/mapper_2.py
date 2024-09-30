
import sys

def mapper():
    """Función mapper que procesa entradas de datos de vuelos y emite el ID del aeropuerto de origen."""
    for line in sys.stdin:
        # Eliminar espacios en blanco y dividir la línea en campos
        line = line.strip()
        fields = line.split(',')

        # Asegurarse de que la línea tenga suficientes campos
        if len(fields) > 15:  # Ajusta según el número total de campos en tus datos
            origin_airport_id = fields[12]  # Suponiendo que OriginAirportID es el campo en la posición 12
            if origin_airport_id.isdigit():
                # Emitir la clave y el valor
                print(f"{origin_airport_id}\t1")

if __name__ == "__main__":
    mapper()
