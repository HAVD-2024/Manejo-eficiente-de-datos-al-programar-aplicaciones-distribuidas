-- query_6.hql

USE flights_db;

-- Consulta para obtener las rutas de vuelo con mayores demoras
SELECT origin, dest, AVG(depdelay) AS Avg_Departure_Delay
FROM raw_flights_data
WHERE depdelay IS NOT NULL
GROUP BY origin, dest
ORDER BY Avg_Departure_Delay DESC
LIMIT 10;