-- query_5.hql

USE flights_db;

-- Consulta para obtener los aeropuertos con más vuelos de partida
SELECT Origin, COUNT(*) AS Total_Flights
FROM raw_flights_data
GROUP BY Origin
ORDER BY Total_Flights DESC;